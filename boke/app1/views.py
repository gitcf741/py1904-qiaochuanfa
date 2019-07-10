
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import *

# Create your views here.

def index(request):
    return render(request,'app1/index.html')
def single(request):
    return render(request,'app1/single.html')
