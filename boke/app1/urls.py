from django.conf.urls import url
from .import views
from .feeds import  ArticleFeed
app_name='app1'


urlpatterns = [
    url('^$',views.IndexView.as_view(),name="index"),
    url('^single/(\d+)/$',views.SingleView.as_view(),name="single"),
    url('^full/$', views.FullView.as_view(), name="full"),

    url('^archives/(\d+)/(\d+)/$', views.ArchivesView.as_view(), name="archives"),

    url('^contact/$', views.ContactView.as_view(), name="contact"),
    url(r'^addarticle/$',views.AddArticleView.as_view(),name="addarticle"),
    # rss订阅
    url(r'^rss/$',ArticleFeed()),

    # url(r'^login/$',views.LoginView.as_view(),name="login")


]
