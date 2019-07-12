from django.contrib import admin
from .models import Question,Chioce
# Register your models here.
class ChioceInline(admin.StackedInline):
    model = Chioce
    extra = 1

class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChioceInline]

admin.site.register(Question,QuestionAdmin)
admin.site.register(Chioce)


