from django.conf.urls import url
from django.conf import settings
from django.contrib.auth import views as auth_views

app_name='account'
urlpatterns = [
	url(r'^login/$', auth_views.LoginView.as_view(template_name='account/login.html'), name="user_login"),
]
