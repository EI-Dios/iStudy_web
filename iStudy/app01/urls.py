from django.urls import path, include, re_path
from app01 import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('register/', views.register, name='register'),
    path('index/', views.index, name='index'),
    re_path('article/(\d+)/', views.article, name='article'),

    # re_path('backstage/', views.backstage, name='backstage'),

    path('article_list/', views.article_list, name='article_list'),
    path('article_add/', views.article_add, name='article_add'),
    re_path('article_edit/(\d+)/', views.article_edit, name='article_edit'),

    path('user_list/', views.user_list, name='user_list'),

    path('category_list/', views.category_list, name='category_list'),
    # path('category_add/', views.category_add, name='category_add'),
    # re_path('category_edit/(\d+)/', views.category_edit, name='category_edit'),

    path('category_add/', views.category_change, name='category_add'),
    re_path('category_edit/(\d+)/', views.category_change, name='category_edit'),

    path('comment/', views.comment, name='comment'),
]
