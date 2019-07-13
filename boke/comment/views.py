from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse
from .models import Comment ,Article

# Create your views here.
class AddComment(View):
    def post(self,request,id):
        print("34")
        name=request.POST.get("name")
        email=request.POST.get("email")
        url=request.POST.get("url")
        content=request.POST.get("content")
        print("12")
        c=Comment()
        c.name=name
        c.email=email
        c.content=content
        print("1123")
        c.article=Article.objects.get(pk=id)
        print("sdf")
        c.save()
        print(c)
        return JsonResponse({"name":c.name,"content":c.content,"create_time":c.create_time})

