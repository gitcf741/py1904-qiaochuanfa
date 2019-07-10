from django.conf.urls import url
from .import views
app_name='app1'

urlpatterns = [
    url('^$',views.index,name="index"),
    url('^single/$',views.single,name="single"),

]