
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from.models import *
from django.shortcuts import *
from django.views.generic import View
from .forms import ArticeForm
from django.core.paginator import Paginator
# Create your views here.

class IndexView(View):
    def get(self,request):
        ads = Ads.objects.all()
        articles = Article.objects.all()
        pagenum=request.GET.get("page")
        pagenum=1 if not pagenum else pagenum
        page=Paginator(articles,3).get_page(pagenum)

        return render(request,'app1/index.html',{'page':page,'ads':ads})

class SingleView(View):
    def get(self,request,id):
        article = Article.objects.all()
        return render(request,'app1/single.html')
    def post(self,request,id):
        return render(request,'app1/single.html')
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
