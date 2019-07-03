from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import BookInfo


# Create your views here.
def index(request):
    # 获取模块
    # return  HttpResponse("这里是首页 <a href='/list/'>跳转</a>")
    temp1=loader.get_template('booktest/index.html')
    book1=BookInfo.objects.all()
    result=temp1.render({"books":book1})
    # 使用模块渲染字典参数
    # result=temp1.render({})
    # 将渲染的结果返回
    return HttpResponse(result)

# def list(request):
#     return  HttpResponse("这里是列表页 <a href='/booktest/detail/'>跳转</a>")
# def detail(request):
#     return  HttpResponse("这里是详情页 <a href='/booktest/index/'>跳转</a>")
def list(request):

    # s="""
    # <a href='/detail/1/'>跳转到详情页1</a>
    # <a href='/detail/2/'>跳转到详情页2</a>
    # <a href='/detail/3/'>跳转到详情页3</a>
    # <a href='/detail/4/'>跳转到详情页4</a>
    # """
    temp2=loader.get_template('booktest/list.html')
    books=BookInfo.objects.all()
    result=temp2.render({"book":books})
    return  HttpResponse(result)



    # return  HttpResponse("这里是列表%s"%(s,))
def detail(request,id):
    temp3=loader.get_template("booktest/detail.html")
    book=BookInfo.objects.get(pk= id)
    result=temp3.render({"book":book})

    return  HttpResponse(result)

    # return  HttpResponse("这里是%s详情页<a href='/'>跳转到首页</a>"%(id,))