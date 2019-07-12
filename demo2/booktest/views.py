from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse
# Create your views here.
from .models import Question,Chioce

# Create your views here.

def index(request):
    questions=Question.objects.all()
    return render(request,"booktest/index.html",locals())

#
def detail(request,id):
    question=Question.objects.get(pk = id)
    if request.method=="GET":
        return render(request,"booktest/detail.html",locals())
    elif request.method=="POST":
        chioceid=request.POST.get("choice")
        chioce=Chioce.objects.get(pk=chioceid)
        chioce.votes+=1
        chioce.save()
        return redirect(reverse("booktest:result", args=(id,)))
def result(request,id):
    question = Question.objects.get(pk = id)
    return render(request,"booktest/result.html",locals())