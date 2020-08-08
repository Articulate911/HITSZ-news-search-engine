from . import views
from django.urls import path

app_name = 'news'

urlpatterns = [
    # path函数将url映射到视图
    path('', views.news_list, name='home'),
    path('news-search/', views.news_search, name='news_search'),
]