from django.shortcuts import render, redirect
from app01 import models
import hashlib
from app01.forms import RegFrom, ArticleForm, CategoryForm
from utils.pagination import Pagination


# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        md5 = hashlib.md5()
        md5.update(password.encode('utf-8'))
        user_obj = models.User.objects.filter(username=username, password=md5.hexdigest(), is_active=True).first()
        if user_obj:
            # 登录成功
            # 保存登录状态
            request.session['is_login'] = True
            request.session['username'] = user_obj.username
            request.session['pk'] = user_obj.pk
            url = request.GET.get('url')
            if url:
                return redirect((url))
            return redirect('index')
        error = '用户名或密码错误'
    return render(request, 'login.html', locals())


def logout(request):
    request.session.delete()
    return redirect('index')


def register(request):
    form_obj = RegFrom()
    if request.method == 'POST':
        form_obj = RegFrom(request.POST, request.FILES)
        if form_obj.is_valid():
            # 注册成功
            form_obj.save()
            return redirect('login')
    return render(request, 'register.html', {'form_obj': form_obj})


def index(request):
    # 查询所有的文章
    all_article = models.Article.objects.all()
    # is_login = request.session.get('is_login')
    # username = request.session.get('username')
    page = Pagination(request, all_article.count(), 3)
    return render(request, 'index.html', {'all_article': all_article[page.start:page.end], 'page_html': page.page_html})


def article(request, pk):
    article_obj = models.Article.objects.get(pk=pk)
    return render(request, 'article.html', {'article_obj': article_obj})


# def backstage(request):
#     return render(request, 'backstage.html')


from django.db.models import Q


# 模糊搜索
def get_query(request, field_list):
    # 传入一个列表，返回一个Q对象
    query = request.GET.get('query', '')
    q = Q()
    # Q(Q(title__contains=query)|Q(detail_content__contains=query))
    q.connector = 'OR'
    for field in field_list:
        q.children.append(Q(('{}__contains'.format(field), query)))
    return q


# 展示文章列表
def article_list(request):
    # query = request.GET.get('query', '')
    from django.http.request import QueryDict
    # request.GET.urlencode()
    # request.GET._mutable = True
    # request.GET['page'] = 1
    q = get_query(request, ['title', 'detail__content', 'create_time'])
    all_articles = models.Article.objects.filter(q, author=request.user_obj)
    page = Pagination(request, all_articles.count(), 3)
    return render(request, 'article_list.html',
                  {'all_articles': all_articles[page.start:page.end], 'page_html': page.page_html})


# 新增文章
def article_add(request):
    form_obj = ArticleForm(request)
    if request.method == 'POST':
        form_obj = ArticleForm(request, request.POST)
        if form_obj.is_valid():
            # 获取文章详情的字符串
            detail = request.POST.get('detail')
            # 创建文章详情的对象
            detail_obj = models.ArticleDetail.objects.create(content=detail)
            form_obj.cleaned_data['detail_id'] = detail_obj.pk
            models.Article.objects.create(**form_obj.cleaned_data)
            return redirect('article_list')
    return render(request, 'article_add.html', {'form_obj': form_obj})


# 编辑文章
def article_edit(request, pk):
    obj = models.Article.objects.filter(pk=pk).first()
    form_obj = ArticleForm(request, instance=obj)
    if request.method == 'POST':
        form_obj = ArticleForm(request, request.POST, instance=obj)
        if form_obj.is_valid():
            form_obj.instance.detail.content = request.POST.get('detail')
            form_obj.instance.detail.save()  # 保存文章详情
            form_obj.save()  # 保存文章的信息
            url = request.GET.get('url')
            if url:
                return redirect(url)
            return redirect('article_list')
    return render(request, 'article_edit.html', {'form_obj': form_obj, 'obj': obj})


users = [{'name': 'wzy-{}'.format(i), 'password': '123'} for i in range(1, 445)]


def user_list(request):
    page = Pagination(request, len(users))
    return render(request, 'user_list.html', {'users': users[page.start:page.end], 'page_html': page.page_html})


def category_list(request):
    q = get_query(request, ['title', 'pk'])
    all_categories = models.Category.objects.filter(q)  # filter（字段名__contains='xxx'）
    return render(request, 'category_list.html', {'all_categories': all_categories})


# def category_add(request):
#     form_obj = CategoryForm()
#     if request.method == 'POST':
#         form_obj = CategoryForm(request.POST)
#         if form_obj.is_valid():
#             form_obj.save()
#             return redirect('category_list')
#     title = '新增分类'
#     return render(request, 'form.html', {'form_obj': form_obj, 'title': title})


# def category_edit(request, pk):
#     obj = models.Category.objects.filter(pk=pk).first()
#     form_obj = CategoryForm(instance=obj)
#     if request.method == 'POST':
#         form_obj = CategoryForm(request.POST, instance=obj)
#         if form_obj.is_valid():
#             form_obj.save()
#             return redirect('category_list')
#     title = '编辑分类'
#     return render(request, 'form.html', {'form_obj': form_obj, 'title': title})


def category_change(request, pk=None):
    obj = models.Category.objects.filter(pk=pk).first()  # pk=None   obj=None
    form_obj = CategoryForm(instance=obj)
    if request.method == 'POST':
        form_obj = CategoryForm(request.POST, instance=obj)
        if form_obj.is_valid():
            form_obj.save()
            return redirect('category_list')
    title = '编辑分类' if pk else '新增分类'
    return render(request, 'form.html', {'form_obj': form_obj, 'title': title})


from django.http.response import JsonResponse
from django.utils import timezone


def comment(request):
    obj = models.Comment.objects.create(**request.GET.dict())
    return JsonResponse({'status': True, 'time': timezone.localtime(obj.time).strftime('%Y-%m-%d %H:%M:%S')})
