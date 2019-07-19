
from django.conf.urls import url
from .models import *
from . import  views
app_name='app'

urlpatterns=[

url('^$',views.IndexView.as_view(),name="index"),
#     导航栏界面
# url('^index/$',views.index,name="login"),

url('^register/$',views.register,name="register"),
url('^login/$',views.login,name="login"),
url('^logout/$', views.logout, name='logout'),
url(r'^verify/$', views.verify, name='verify'),
url('^item_show/(\d+)/$',views.item_show,name="item_show"),


url('^udai_notice/(\d+)/$',views.udai_notice.as_view(),name='udai_notice'),

url('^udai_welcome/$',views.udai_welcome,name='udai_welcome'),
url('^udai_order/$',views.udai_order,name='udai_order'),
url('^udai_integral/$',views.udai_integral,name='udai_integral'),

url('^udai_shopcart/$',views.udai_shopcart,name='udai_shopcart'),
url('^class_room/$',views.class_room,name='class_room'),


url('^udai_article10/$',views.udai_article10,name='udai_article10'),
url('^udai_article5/$',views.udai_article5,name='udai_article5'),
url('^udai_contract/$',views.udai_contract,name='udai_contract'),
url('^item_remove/$',views.item_remove,name='item_remove'),
url('^enterprise_id/$',views.enterprise_id,name='enterprise_id'),

url('^udai_article1/$',views.udai_article1,name='udai_article1'),
url('^udai_article2/$',views.udai_article2,name='udai_article2'),
url('^udai_article3/$',views.udai_article3,name='udai_article3'),
url('^udai_article4/$',views.udai_article4,name='udai_article4'),
url('^udai_article5/$',views.udai_article5,name='udai_article5'),
url('^udai_article6/$',views.udai_article6,name='udai_article6'),
url('^udai_article7/$',views.udai_article7,name='udai_article7'),
url('^udai_article8/$',views.udai_article8,name='udai_article8'),
url('^udai_article10/$',views.udai_article10,name='udai_article10'),
url('^udai_article11/$',views.udai_article11,name='udai_article11'),
url('^udai_article12/$',views.udai_article12,name='udai_article12'),

url('^udai_setting/$',views.udai_setting,name='udai_setting'),
url('^udai_treasurer/$',views.udai_treasurer,name='udai_treasurer'),
url('^udai_address/$',views.udai_address,name='udai_address'),
url('^udai_coupon/$',views.udai_coupon,name='udai_coupon'),
url('^udai_paypwd_modify/$',views.udai_paypwd_modify,name='udai_paypwd_modify'),
url('^udai_pwd_modify/$',views.udai_pwd_modify,name='udai_pwd_modify'),
url('^udai_refund/$',views.udai_refund,name='udai_refund'),
url('^udai_collection/$',views.udai_collection,name='udai_collection'),



]