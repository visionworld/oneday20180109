from django.conf.urls import url

from app01 import views

urlpatterns = [
    # 创建首页ｕｒｌ路径
    url(r'^index/$', views.index),
    # 创建静态文件显示ｕｒｌ路径
    url(r'^show_static/$', views.show_static)
]
