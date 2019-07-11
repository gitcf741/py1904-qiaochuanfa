import xadmin
from .models import *
# Register your models here.
xadmin.site.register(Category)
class ArticleAdmin:
    style_fields={"body":"ueditor"}
xadmin.site.register(Article,ArticleAdmin)
xadmin.site.register(Tag)
xadmin.site.register(Ads)