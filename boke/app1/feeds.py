from django.contrib.syndication.views import Feed
from .models import *
from django.shortcuts import reverse
class ArticleFeed(Feed):
    title="zzy的博客"
    description ="介绍了一些开发知识"
    link="/"

    def items(self):
        return  Article.objects.order_by("-create_time")[:3]

    def item_title(self,item):
        return  item.title

    def item_link(self, item):
        return reverse('app1:single',args=(item))

    def item_description(self, item):

        return  item.author.username + ":"+ item.title

