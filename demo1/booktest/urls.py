from . import views
from django.conf.urls import url
urlpatterns=[
        url(r'^$',views.index),
        url(r'^list/$',views.list),
        url(r'^detail/(\d+)/$',views.detail),
    ]