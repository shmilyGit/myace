"""leace URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from django.views.generic import TemplateView
from account import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^account/', include('account.urls', namespace='account')),

#登录之后跳转到该页,该页即首页
    url(r'^index/', auth_views.ShowIndexPageView.as_view(), name='show_index'),

#直接访问IP:port 后边不用加路径, 即http://192.168.5.105:8000就会跳转到login.html
#方法一,这样不会在html模板中使用{{form.password}}
		#url('', TemplateView.as_view(template_name="account/login.html"), name='loginPage'),
#方法二,这样可以在html模板中使用{{form.password}}
		url('', auth_views.LoginView.as_view(template_name='account/login.html'), name="loginPage"),
]
