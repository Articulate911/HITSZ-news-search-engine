from django.shortcuts import render
# from django.http import HttpResponse
from .models import News
import pymysql
import jieba


def news_list(request):
    news = News.objects.all()
    print(type(news))
    return render(request, 'news/list.html',{'news': news})

def news_search(request):
    q = request.GET.get('q')
    if not q:
        q = '哈尔滨工业大学（深圳）'
    search_method = request.GET.get('search_method')
    if not search_method:
        search_method = '0'
    db = pymysql.connect("localhost","root","123","hitsz")
    if search_method=='0':
        search_method='模糊查询'
        word_sep=jieba.lcut_for_search(q)
        sql = "SELECT * FROM news WHERE "
        for word in word_sep:
            sql = sql + "title like \'%" + word + "%\' or "
        sql = sql[:-4]
    else:
        search_method='精确查询'
        sql = "SELECT * FROM news WHERE title like \'%"+q+"%\'"
    cursor = db.cursor()
    cursor.execute(sql)
    news_list=cursor.fetchall()
    row_count = cursor.rowcount
    News_list=[]
    for newspiece in news_list:
        news=News()
        news.title=newspiece[2]
        news.url=newspiece[1]
        news.date=newspiece[3]
        News_list.append(news)
    return render(request, 'news/search.html', {'query':q,\
                                                'search_method':search_method,\
                                                'result_cnt':row_count,\
                                                'news_search': News_list\
                                                })
