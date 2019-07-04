from . import views
from django.conf.urls import url
app_name='booktest'
urlpatterns=[
        url(r'^$',views.index,name="index"),
        url(r'^list/$',views.list,name="list"),
        url(r'^detail/(\d+)/$',views.detail,name="detail"),
        url(r'^deletehero/(\d+)/$',views.deletehero,name="deletehero"),
        # url(r'^addbook/(\d+)$',views.deletehero,name="addbook"),
    ]