from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import redirect, reverse
import re
from app01 import models

class AuthMiddleWare(MiddlewareMixin):
    def process_request(self, request):
        # 需要登录后访问的地址 需要判断登录状态
        # 默认所有的地址都要登录才能访问
        # 设置一个白名单 不登录就能访问
        url = request.path_info

        # 校验登录状态
        is_login = request.session.get('is_login')
        if is_login:
            # 已经登录  可以访问
            obj = models.User.objects.filter(pk=request.session['pk']).first()
            request.user_obj = obj
            return
        # 白名单
        for i in [
            r'^/login/$',
            r'^/index/$',
            r'^/register/$',
            r'^/article/\d+$',
        ]:
            if re.match(i, url):
                return
            # 没有登录 需要去登录
        return redirect('{}?url={}'.format(reverse('login'), url))
