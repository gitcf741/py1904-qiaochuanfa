from django.contrib import admin
from .models import *

class HeroInfoINlines(admin.StackedInline):
    model = HeroInfo
    extra = 4

class BookInfoAdmin(admin.ModelAdmin):
    list_display =('tile','pub_date')
    list_per_page = 1
    inlines = [HeroInfoINlines,]

# Register your models here.

admin.site.register(BookInfo)

class HeroInfoAdmin(admin.ModelAdmin):
    list_display = ["name","content"]
    search_fields = ["name","content"]


admin.site.register(HeroInfo,HeroInfoAdmin)