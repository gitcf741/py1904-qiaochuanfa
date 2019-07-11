"""自定义模板表达式扩展Django原有的功能"""
from django.template import library
register=library.Library()
from app1.models import Article
@register.simple_tag
def getlatestarticles(num):
    # f返回最新的文章num=3
        return Article.objects.order_by("-create_time")[:num]
