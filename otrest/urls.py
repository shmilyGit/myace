from django.conf.urls import url
from django.conf import settings
from django.views.generic import TemplateView
from . import views as otrest_views

app_name='otrest'
urlpatterns = [
	url(r'^otrequest/$', otrest_views.OtRequestView.as_view(), name="otrequest"),
	url(r'^save-otrequest/$', otrest_views.OtRequestView.as_view(), name="save_otrequest"),
	url(r'^list-otrequest/$', otrest_views.OtRequestListView.as_view(), name="list_otrequest"),
	url(r'^del-otrequest/(?P<pk>\d+)$', otrest_views.OtRequestDeleteView.as_view(), name="del_otrequest"),
	#url(r'^edit-otrequest/$', otrest_views.OtRequestUpdateView.as_view(), name="edit_otrequest"),
]
