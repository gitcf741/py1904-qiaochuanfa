"""boke URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from django.views.static import serve
from .settings import MEDIA_ROOT
import xadmin
urlpatterns = [
    path('admin/', admin.site.urls),
    # path('xadmin/', xadmin.site.urls),

    url('',include('app1.urls',namespace="app1")),

    url('',include('comment.urls',namespace="comment")),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),
    # 空任意匹配
    path('ueditor/', include('DjangoUeditor.urls')),

    url('search/',include('haystack.urls')),

]
