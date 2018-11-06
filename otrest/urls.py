from django.conf.urls import url
from django.conf import settings
from django.views.generic import TemplateView
from . import views as otrest_views

app_name='otrest'
urlpatterns = [
	url(r'^ot-request/$', otrest_views.OtRequestView.as_view(), name="ot_request"),
	url(r'^save-otrequest/$', otrest_views.OtRequestView.as_view(), name="save_otrequest"),
]
