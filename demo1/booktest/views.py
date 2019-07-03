from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return  HttpResponse("这里是首页 <a href='/list/'>跳转</a>")
# def list(request):
#     return  HttpResponse("这里是列表页 <a href='/booktest/detail/'>跳转</a>")
# def detail(request):
#     return  HttpResponse("这里是详情页 <a href='/booktest/index/'>跳转</a>")
def list(request):
    s="""
    <a href='/detail/1/'>跳转到详情页1</a>
    <a href='/detail/2/'>跳转到详情页2</a>
    <a href='/detail/3/'>跳转到详情页3</a>
    <a href='/detail/4/'>跳转到详情页4</a>
    """
    return  HttpResponse("这里是列表%s"%(s,))
def detail(request,id):
    return  HttpResponse("这里是%s详情页<a href='/'>跳转到首页</a>"%(id,))