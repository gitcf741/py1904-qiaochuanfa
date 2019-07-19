from django.shortcuts import render,redirect,reverse
from . import models
from . models import *
from django.core.paginator import Paginator,Page
from django.views import View
from django.http import HttpResponse
from PIL import Image,ImageDraw,ImageFont
import random,io
from django.core.cache import cache
from django.views.decorators.cache import cache_page


# Create your views here.



def getpage(request,object_list,per_num):
    pagenum = request.GET.get("page")
    pagenum = 1 if not pagenum else pagenum
    page = Paginator(object_list, per_num).get_page(pagenum)
    return page




class IndexView(View):
    def get(self,request):
        ads = Ads.objects.all()
        sp=Cart.objects.all()
        # name=request.session.get('username')
        content=Title.objects.all()
        return render(request,'app/index.html',locals())




def register(request):
    if request.method == "GET":
        return render(request,'app/register.html',{'msg':"请填入以下信息"})
    elif request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        password1 = request.POST.get("password2")
        for a in  User.objects.all():
            print(a)
            if username ==a.name:
                return  render(request,'app/register.html',{"msg":"用户名已使用"})

            if len(username) == 0:
                return render(request,'app/register.html',{'msg':"用户名不能为空"})
            if len(password)< 6:
                return render(request,'app/register.html',{'msg':"密码不能小于6位"})
            if password != password1:
                return render(request,'app/register.html',{'msg':"两次密码输入不一致"})

        try:
            user = User()
            user.name = username
            user.passworld = password
            user.passworld1 = password1
            user.save()
            return  redirect(reverse('app:login'))
        except:
            return redirect(reverse('app:register'))





def login(request):
    if request.method=="GET":
        return  render(request,"app/login.html")

    elif request.method=="POST":

        username = request.POST.get("username")
        password = request.POST.get("password")


        user = User.objects.filter(name=username, passworld=password).first()
        verifycode = request.POST.get("verify")
        if not verifycode == cache.get("verify"):
            return render(request,'app/login.html',locals())

        # user = authenticate(request, name=username, passworld=password)
        print('--------------', username, password, user)
        try:
            if user.static == 0:
                result = User.objects.all().filter(name=username).update(static=1)
                # result.save()
                # login(request,user)
                # request.session['username'] = "已登录"
                request.COOKIES["zzy"]="已登录"



                return redirect(reverse('app:index'))
            else:
                return render(request, 'app/login.html', {"msg": "账户已经登录"})
        except:
            return  render(request,'app/login.html')
        # user = User.objects.filter(name=username, passworld=password).first()
        # print('--------------', username,password,user)
        # if user.static == 0:
        #     result = User.objects.all().filter(name=username).update(static=1)
        #     # result.save()
        #     return redirect(reverse('app:index'))
        # else:
        #     return render(request, 'app/login.html', {"msg": "账户已经登录"})


def logout(request):
    result = User.objects.all().update(static=0)
    # result.save()
    # return render(request,'app/index.html')
    return redirect(reverse('app:login'))

def verify(request):
    # 返回固定图片
    # with open("static/img/2.png","rb") as f:
    #     content = f.read()
    #     return HttpResponse(content)

    # 定义变量，用于画面的背景色、宽、高
    bgcolor = (random.randrange(20, 100),
               random.randrange(20, 100),
               random.randrange(20, 100))
    width = 100
    heigth = 35
    # 创建画面对象
    im = Image.new('RGB', (width, heigth), bgcolor)
    # 创建画笔对象
    draw = ImageDraw.Draw(im)
    # 调用画笔的point()函数绘制噪点
    for i in range(0, 100):
        xy = (random.randrange(0, width), random.randrange(0, heigth))
        fill = (random.randrange(0, 255), 255, random.randrange(0, 255))
        draw.point(xy, fill=fill)
    # 定义验证码的备选值
    str1 = 'ABCD123EFGHIJK456LMNOPQRS789TUVWXYZ0'
    # 随机选取4个值作为验证码
    rand_str = ''
    for i in range(0, 4):
        rand_str += str1[random.randrange(0, len(str1))]
    cache.set("verify",rand_str)
    # 构造字体对象
    font = ImageFont.truetype('calibrib.ttf', 30)
    fontcolor = (255, random.randrange(0, 255), random.randrange(0, 255))
    # 绘制4个字
    draw.text((5, 2), rand_str[0], font=font, fill=fontcolor)
    draw.text((25, 2), rand_str[1], font=font, fill=fontcolor)
    draw.text((50, 2), rand_str[2], font=font, fill=fontcolor)
    draw.text((75, 2), rand_str[3], font=font, fill=fontcolor)
    # 释放画笔
    del draw
    # request.session['verifycode'] = rand_str
    f = io.BytesIO()
    im.save(f, 'png')
    # 将内存中的图片数据返回给客户端，MIME类型为图片png
    return HttpResponse(f.getvalue(), 'image/png')



def item_show(request,id):
        shop=Cart.objects.get(pk=id)
        return  render(request,'app/item_show.html',{'shop':shop})

def udai_order(request):

    return  render(request,'app/udai_order.html')

# return render(request, 'app/udai_notice.html')
class udai_notice(View):

    def get(self, request,id):
        title = Title.objects.get(pk=id)
        title1=Title.objects.all()
        return render(request, 'app/udai_notice.html',{ "title":title,"title1":title1})

    # def post(self,request,id):
    #     return redirect(reverse('app1:udai_notice',args=(id,)))











def udai_welcome(request):
    return  render(request,'app/udai_welcome.html')



def udai_integral(request):
    return  render(request,'app/udai_integral.html')
def udai_shopcart(request):
    return  render(request,'app/udai_shopcart.html')
def class_room(request):
    return  render(request,'app/class_room.html')
def udai_article10(request):
    return  render(request,'app/udai_article10.html')
def udai_article5(request):
    return  render(request,'app/udai_article5.html')
def udai_contract(request):
    return  render(request,'app/udai_contract.html')
def item_remove(request):
    return  render(request,'app/item_remove.html')
def enterprise_id(request):
    return  render(request,'app/enterprise_id.html')

def udai_article1(request):
    return  render(request,'app/udai_article1.html')
def udai_article2(request):
    return  render(request,'app/udai_article2.html')
def udai_article3(request):
    return  render(request,'app/udai_article3.html')
def udai_article4(request):
    return  render(request,'app/udai_article4.html')
def udai_article5(request):
    return  render(request,'app/udai_article5.html')
def udai_article6(request):
    return  render(request,'app/udai_article6.html')
def udai_article7(request):
    return  render(request,'app/udai_article7.html')
def udai_article8(request):
    return  render(request,'app/udai_article8.html')
def udai_article10(request):
    return  render(request,'app/udai_article10.html')
def udai_article11(request):
    return  render(request,'app/udai_article11.html')
def udai_article12(request):
    return  render(request,'app/udai_article12.html')

def udai_setting(request):
    return  render(request,'app/udai_setting.html')
def udai_treasurer(request):
    return  render(request,'app/udai_treasurer.html')
def udai_integral(request):
    return  render(request,'app/udai_integral.html')
def udai_address(request):
    return  render(request,'app/udai_address.html')
def udai_coupon(request):
    return  render(request,'app/udai_coupon.html')
def udai_paypwd_modify(request):
    return  render(request,'app/udai_paypwd_modify.html')

def udai_collection(request):
    return  render(request,'app/udai_collection.html')
def udai_refund(request):
    return  render(request,'app/udai_refund.html')
def udai_pwd_modify(request):
    return  render(request,'app/udai_pwd_modify.html')
