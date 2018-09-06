from django.conf.urls import url
from django.conf import settings
from django.contrib.auth import views as auth_views

app_name='account'
urlpatterns = [
	#注意基本类的视图的写法 .as_view(template_name= TemplateName),不再是{"template_name":"account/logout.html"},后者是基于视图的写法
	#django2.1已经使用基于类的视图代替了基于函数的视图
	#url(r'^logout/$', auth_views.LogoutView.as_view, {"template_name":"account/logout.html"}, name="user_logout"),

	url(r'^login/$', auth_views.LoginView.as_view(template_name='account/login.html'), name="user_login"),
	url(r'^password-change/$', auth_views.PasswordChangeView.as_view(), name="password_change"),
]
