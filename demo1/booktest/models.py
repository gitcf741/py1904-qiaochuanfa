from django.db import models

# Create your models here.

class BookInfo(models.Model):
    tile=models.CharField(max_length=20)
    pub_date=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.tile

class HeroInfo(models.Model):
    name=models.CharField(max_length=20)
    # gender=models.CharField(default=True)
    gender=models.CharField(max_length=5,choices=(("man","男"),("women","女")))
    type=models.CharField(max_length=5,choices=(("man","男"),("women","女")),default="man")
    content=models.CharField(max_length=100)
    book=models.ForeignKey(BookInfo,on_delete=models.CASCADE)
    def __str__(self):
        return self.name
    def __str__(self):
        return self.content
