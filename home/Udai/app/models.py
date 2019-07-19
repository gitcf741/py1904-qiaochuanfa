from django.db import models

# Create your models here.
class User(models.Model):
    name=models.CharField(max_length=10)
    passworld=models.CharField(max_length=20)
    passworld1=models.CharField(max_length=20)
    static=models.IntegerField(default=0)
    def __str__(self):
        return self.name




class Ads(models.Model):
    # 图片存放位置
    image=models.ImageField(upload_to='ads')
    desc=models.CharField(max_length=10)
    index=models.IntegerField(default=0)
    def __str__(self):
        return self.desc
# 分类
class Ads1(models.Model):
    # 图片存放位置
    image1=models.ImageField(upload_to='ads1')
    desc=models.CharField(max_length=10)
    index=models.IntegerField(default=0)
    def __str__(self):
        return self.desc

class Ads2(models.Model):
    # 图片存放位置
    image2=models.ImageField(upload_to='ads2')
    desc=models.CharField(max_length=10)
    index=models.IntegerField(default=0)
    def __str__(self):
        return self.desc



class Cart(models.Model):
    image=models.ImageField(upload_to="sp")
    desc=models.CharField(max_length=200)
    price=models.IntegerField(default=0)
    create_time=models.TimeField(auto_now_add=True)
    uper_time=models.TimeField(auto_now=True)
    def __str__(self):
        return  self.desc
class Detail(models.Model):
    img0=models.ImageField(upload_to='detail',null=True)
    # img1=models.ImageField(upload_to='detail/ads',null=True)
    # img2=models.ImageField(upload_to='detail/content',null=True)
    color=models.CharField(max_length=20,null=True)
    color1=models.CharField(max_length=5,default="红色")
    color2=models.CharField(max_length=5,default="白色")
    color3=models.CharField(max_length=5,default="黑色")
    color4=models.CharField(max_length=5,default="粉色")
    color5=models.CharField(max_length=5,default="灰色")
    size=models.CharField(max_length=5,default="墨绿色")
    num=models.IntegerField(null=False)
    vip=models.IntegerField(default=0)
    sales=models.IntegerField(default=0,null=False)
    integral=models.IntegerField(default=0,null=False)
    cart=models.ForeignKey(Cart,on_delete=models.CASCADE)

class Comment(models.Model):
    name = models.CharField(max_length=20)
    url = models.URLField(blank=True, null=True, default="http://baidu.com")
    email = models.EmailField(blank=True, null=True)
    content = models.TextField()
    create_time = models.DateTimeField(auto_now_add=True)
    article = models.ForeignKey(Cart,on_delete=models.CASCADE)
class Title(models.Model):
    title=models.CharField(max_length=20,null=True)
    create_time=models.TimeField(auto_now_add=True)
class Notice(models.Model):
    body=models.CharField(max_length=500,null=False)
    content=models.ForeignKey(Title,on_delete=models.CASCADE)




