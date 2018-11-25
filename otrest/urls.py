from django.conf.urls import url
from django.conf import settings
from django.views.generic import TemplateView
from . import views as otrest_views

app_name='otrest'
urlpatterns = [
    ## 加班申请
	url(r'^otrequest/$', otrest_views.OtRequestCreateView.as_view(), name="otrequest"),
	url(r'^list-otrequest/$', otrest_views.OtRequestListView.as_view(), name="list_otrequest"),
	url(r'^delete-otrequest/(?P<pk>\d+)$', otrest_views.OtRequestDeleteView.as_view(), name="delete_otrequest"),
	url(r'^detail-otrequest/(?P<pk>\d+)$', otrest_views.OtRequestDetailView.as_view(), name="detail_otrequest"),
	url(r'^update-otrequest/(?P<pk>\d+)$', otrest_views.OtRequestUpdateView.as_view(), name="update_otrequest"),

    ## 加班凭证提交
	url(r'^create-otrecord/$', otrest_views.OtRecordCreateView.as_view(), name="create_otrecord"),
]
