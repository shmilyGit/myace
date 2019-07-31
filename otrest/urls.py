from django.urls import path,re_path
from django.conf.urls import url
from django.conf import settings
from django.views.generic import TemplateView
from . import views as otrest_views

app_name='otrest'
urlpatterns = [
    ## 加班申请
	path('create-otrequest/', otrest_views.OtRequestCreateView.as_view(), name="create_otrequest"),
	path('list-otrequest/', otrest_views.OtRequestListView.as_view(), name="list_otrequest"),
	re_path(r'^delete-otrequest/(?P<pk>\d+)$', otrest_views.OtRequestDeleteView.as_view(), name="delete_otrequest"),
	re_path(r'^detail-otrequest/(?P<pk>\d+)$', otrest_views.OtRequestDetailView.as_view(), name="detail_otrequest"),
	re_path(r'^update-otrequest/(?P<pk>\d+)$', otrest_views.OtRequestUpdateView.as_view(), name="update_otrequest"),

    ## 加班凭证提交
	re_path(r'^create-otrecord/(?P<pk>\d+)$', otrest_views.OtRecordCreateView.as_view(), name="create_otrecord"),
	path('list-otrecord/', otrest_views.OtRecordListView.as_view(), name="list_otrecord"),
]
