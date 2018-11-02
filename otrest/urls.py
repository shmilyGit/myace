from django.conf.urls import url
from django.conf import settings
from django.views.generic import TemplateView
from . import views as otrest_views

app_name='otrest'
urlpatterns = [
	url(r'^ot-request/$', otrest_views.OtRestView.as_view(), name="ot_request"),
]
