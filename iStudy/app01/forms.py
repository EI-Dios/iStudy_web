from app01 import models
from django import forms
from django.core.exceptions import ValidationError
import hashlib


class RegFrom(forms.ModelForm):
    password = forms.CharField(error_messages={'required': '必填项，且密码长度不能小于6位'},
                               widget=forms.PasswordInput(attrs={'placeholder': '密码', 'type': 'password'}), label='密码',
                               min_length=6)
    re_password = forms.CharField(error_messages={'required': '必填项，要与密码一致'},widget=forms.PasswordInput(attrs={'placeholder': '确认密码', 'type': 'password'}),
                                  label='确认密码', min_length=6)

    class Meta:
        model = models.User
        fields = '__all__'  # ['username', 'password']
        exclude = ['last_time', 'is_active']
        # labels = {
        #     'username': '用户名'
        # }
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': '用户名', 'autocomplete': 'off'}),
            'position': forms.TextInput(attrs={'placeholder': '请输入职位'}),
            # 'company':forms.Select(),
            'phone': forms.TextInput(attrs={'placeholder': '手机号'}),
        }
        error_messages = {
            'username': {
                'required': '必填项',
            },
            'password': {
                'required': '必填项',
            },
            're_password': {
                'required': '必填项',
            },
            'position': {
                'required': '必填项',
            },
            'company': {
                'required': '必选项',
            },
            'phone': {
                'required': '必填项',
            },
        }

    def clean_phone(self):
        import re
        phone = self.cleaned_data.get('phone')
        if re.match(r'1[3-9]\d{9}$', phone):
            return phone
        raise ValidationError('手机号格式不正确')

    def clean(self):
        self._validate_unique = True  # 数据库检验唯一
        password = self.cleaned_data.get('password', '')
        re_password = self.cleaned_data.get('re_password')
        if password == re_password:
            md5 = hashlib.md5()
            md5.update(password.encode('utf-8'))
            self.cleaned_data['password'] = md5.hexdigest()
            return self.cleaned_data
        self.add_error('re_password', '两次密码不一致！')
        raise ValidationError('两次密码不一致')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 自定义操作
        field = self.fields['company']
        choices = field.choices
        choices[0] = ('', '请选择公司')
        field.choices = choices


class ArticleForm(forms.ModelForm):
    class Meta:
        model = models.Article
        fields = "__all__"
        exclude = ['detail']

    def __init__(self, request, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 自定义操作
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

        # 修改choices的参数
        self.fields['author'].choices = [(request.user_obj.pk, request.user_obj.username)]

class CategoryForm(forms.ModelForm):
    class Meta:
        model = models.Category
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 自定义操作
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
