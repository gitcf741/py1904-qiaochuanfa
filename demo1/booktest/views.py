from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import BookInfo,HeroInfo
from django.shortcuts import *



# Create your views here.
def index(request):

    # 获取模块
    # return  HttpResponse("这里是首页 <a href='/list/'>跳转</a>")
    # temp1=loader.get_template('booktest/index.html')
    # book1=BookInfo.objects.all()
    # result=temp1.render({})
    # 使用模块渲染字典参数
    # result=temp1.render({})
    # 将渲染的结果返回
    return render(request,"booktest/index.html",{"username":"zzy"})


# def list(request):
#     return  HttpResponse("这里是列表页 <a href='/booktest/detail/'>跳转</a>")
# def detail(request):
#     return  HttpResponse("这里是详情页 <a href='/booktest/index/'>跳转</a>")
def list(request):
    # temp2=loader.get_template('booktest/list.html')
    books=BookInfo.objects.all()
    # result=temp2.render({"book":books})
    # return  HttpResponse(result)
    return  render(request,"booktest/list.html",{"book":books})



    # return  HttpResponse("这里是列表%s"%(s,))
def detail(request,id):
    # temp3=loader.get_template("booktest/detail.html")
    # book=BookInfo.objects.get(pk = id)
    # result=temp3.render({"book":book})
    # return  HttpResponse(result)

    book=BookInfo.objects.get(pk=id)
    return render(request,"booktest/detail.html",{"book":book})

    # return  HttpResponse("这里是%s详情页<a href='/'>跳转到首页</a>"%(id,))
def deletebook(request,id):
    Book=BookInfo.objects.get(pk = id)
    Book.delete()
    return redirect(reverse("booktest:list",))



def deletehero(request,id):
    hero =HeroInfo.objects.get(pk =id)
    bookid=hero.book.id
    hero.delete()
    #
    return  redirect(reverse("booktest:detail",args=(bookid,)))

    # return HttpResponse("SHNSDF")
    # return  HttpResponseRedirect("/detail/"+ str(bookid)+ "/")
#
def addhero(request,id):
    book = BookInfo.objects.get(pk = id)
    if request.method == "GET":
        return render(request,"booktest/addhero.html",{"book":book})
    elif request.method == "POST":
        name = request.POST.get("username")
        content = request.POST.get("content")
        gender = request.POST.get("gender")
        gender1 = request.POST.get("gender1")
        hero = HeroInfo()
        hero.name = name
        hero.content = content
        hero.book = book
        hero.gender=gender
        hero.type=gender1
        hero.save()
        return redirect(reverse("booktest:detail",args=(id,)))


def addBook(request):
        if request.method == "GET":
            return render(request, "booktest/addBook.html")
        elif request.method == "POST":
            tile = request.POST.get("title")
            hero = BookInfo()
            hero.tile = tile
            hero.save()
            return redirect(reverse("booktest:list"))



