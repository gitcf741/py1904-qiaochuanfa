
from django.shortcuts import render,get_object_or_404,redirect,reverse
from django.http import HttpResponse
from django.template import loader
from.models import *
from django.views.generic import View
from .forms import ArticeForm,CommentForm
from django.core.paginator import Paginator
# Create your views here.

def getpage(request,object_list,per_num):
    pagenum=request.GET.get("page")
    pagenum= 1 if not pagenum else pagenum
    page=Paginator(object_list,per_num).get_page(pagenum)
    return page

class IndexView(View):
    def get(self,request):
        ads = Ads.objects.all()
        articles = Article.objects.all()
        # pagenum=request.GET.get("page")
        # pagenum=1 if not pagenum else pagenum
        # page=Paginator(articles,3).get_page(pagenum)
        page=getpage(request,articles,3)
        return render(request,'app1/index.html',{'page':page,'ads':ads})

class SingleView(View):
    def get(self,request,id):
        article = get_object_or_404(Article,pk = id)
        article.views+=1
        article.save()

        cf=CommentForm()
        return render(request,'app1/single.html',{"article":article,"cf":cf})
    def post(self,request,id):
        article = get_object_or_404(Article, pk=id)
        cf=CommentForm(request.POST)
        comment=cf.save(commit=False)
        comment.article=article
        comment.save()
        return redirect(reverse("app1:single",args=(article.id,)))
class AddArticleView(View):
    def get(self,request):
        af = ArticeForm()
        return render(request,'app1/addarticle.html',locals())
    def post(self,request):
        af = ArticeForm(request.POST)

        if af.is_valid():

            article = af.save(commit=False)
            article.category = Category.objects.first()
            article.author = User.objects.first()
            article.save()
            return redirect(reverse('app1:index'))
        return HttpResponse("添加失败")
class FullView(View):
    def get(self, request):
        return render(request,'app1/full-width.html')

class ContactView(View):
    def get(self, request):
        return render(request, 'app1/contact.html')

class ArchivesView(View):
    def get(self,request,year,month):
        articles=Article.objects.filter(create_time__year=year,create_time__month=month)
        page = getpage(request,articles,3)
        return  render(request,"app1/index.html",{"page":page,"articles":articles})


