# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    print('这是首页')
    return HttpResponse('ｉｎdex首页')


def show_static(request):
    # 进入静态文件演示界面
    return render(request, 'app01/show_static.html')