from django.shortcuts import render
from .models import Article


# Create your views here.
def homeView(request):
    article_list = Article.objects.all()
    return render(request, 'index.html',
    context={'article_list' : article_list })


def categoryView(request, type = 0):
    if(type == 1):
        article_list = Article.objects.filter(type = 1).values()
    elif(type == 2):
        article_list = Article.objects.filter(type = 2).values()
    elif(type == 3):
        article_list = Article.objects.filter(type = 3).values()
    elif(type == 4):
        article_list = Article.objects.filter(type = 4).values()
    elif(type == 5):
        article_list = Article.objects.filter(type = 5).values()
    elif(type == 6):
        article_list = Article.objects.filter(type = 6).values()
    elif(type == 7):
        article_list = Article.objects.filter(type = 7).values()
    elif(type == 8):
        article_list = Article.objects.filter(type = 8).values()
    # elif(id == 9):
    #     article_list = Article.objects.filter(type = 9).values()
    elif(type == 10):
        article_list = Article.objects.filter(type = 10).values()
    elif(type == 11):
        article_list = Article.objects.filter(type = 11).values()
    elif(type == 12):
        article_list = Article.objects.filter(type = 12).values()
    elif(type == 13):
        article_list = Article.objects.filter(type = 13).values()
    else:
        article_list = Article.objects.all()


    return render(request, 'index.html', context = {'article_list' : article_list})



def newsDesc(request, id):
    curr_article = Article.objects.get(id = id)
    return render(request, 'news_desc.html', context={'curr_article' : curr_article})