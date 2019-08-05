from django.shortcuts import render, redirect
from braces.views import LoginRequiredMixin
from django.views.generic import CreateView, ListView, DeleteView, UpdateView, DetailView
from django.views.generic.base import TemplateView
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.http import HttpResponse, JsonResponse
from django.core.exceptions import ObjectDoesNotExist
import json

from .models import OtRequest, OtRecord
from .forms import OtRequestForm, OtRecordForm
from django.conf import settings

# Create your views here.
## 加班申请 开始
class OtRequestCreateView(LoginRequiredMixin, CreateView):
    login_url = "/account/login/"
    fields = ['ottime', 'reason']
    template_name = 'otrest/otrequest_create.html'
    extra_context = {'m2':'active open', 'm2s1':'active'}

    ##Note1 当继承的是TemplateView时使用这个
    ##def get(self, request):
    ##    return render(request, "otrest/otrequest_create.html")
    
    ##Note2 当继承的是CreateView时使用这个,功能与Note1是一样的,只是两种不同的实现方式
    queryset = OtRequest.objects.all()

    def post(self, request, *args, **kwargs):
        otrequest_form = OtRequestForm(request.POST)

        if otrequest_form.is_valid():
            form_cd = otrequest_form.cleaned_data 
            new_otrequest = otrequest_form.save(commit=False)
            new_otrequest.user = request.user
            new_otrequest.approve = True 
            new_otrequest.save(form_cd)
            return redirect("otrest:list_otrequest")

        return self.render_to_response({"form":otrequest_form})

class OtRequestListView(LoginRequiredMixin, TemplateView):
    login_url = "/account/login/"
    template_name = 'otrest/otrequest_list.html'
    extra_context = {'m2':'active open', 'm2s2':'active'}

    def get(self, request):
        return render(request, self.template_name, self.extra_context)

    def post(self, request, *args, **kwargs):
        page = request.POST.get('page')
        rows = request.POST.get('limit')

        i = (int(page) - 1) * int(rows)
        j = (int(page) - 1) * int(rows) + int(rows)

        otrequests = OtRequest.objects.filter(user = self.request.user)
        total = otrequests.count()

        otrequests = otrequests[i:j]

        dict = []
        resultdict = {}

        for tmp in otrequests:
            dic = {}
            dic['id'] = tmp.id
            dic['ottime'] = tmp.ottime
            dic['reason'] = tmp.reason
            dic['approve'] = tmp.approve
            dic['created'] = tmp.created.strftime("%Y-%m-%d %H:%M:%S")

            try:
                otrequestObj = OtRecord.objects.get(otrequest = tmp.id) 
                if otrequestObj:  
                    dic['isCommit'] = True
            except ObjectDoesNotExist:
                dic['isCommit'] = False
                if tmp.approve:
                    dic['commitUrl'] = "/otrest/create-otrecord/"

            dict.append(dic)

        resultdict['code'] = 0
        resultdict['msg'] = ""
        resultdict['count'] = total 
        resultdict['data'] = dict

        return JsonResponse(resultdict, safe=False) 


class OtRequestDeleteView(LoginRequiredMixin, DeleteView):
    login_url = "/account/login/"
    success_url = reverse_lazy("otrest:list_otrequest")
    model = OtRequest

    def dispatch(self, *args, **kwargs):
        resp = super(OtRequestDeleteView, self).dispatch(*args, **kwargs)

        if self.request.is_ajax():
            response_data = {"result":"ok"}
            return HttpResponse(json.dumps(response_data), content_type="application/json")
        else:
            return resp

class OtRequestDetailView(LoginRequiredMixin, DetailView):
    login_url = "/account/login/"
    template_name = "otrest/layer_otrequest_edit.html"
    context_object_name = "otrequest"

    model = OtRequest

    ##下边注释的两个函数其实放开效果是一样的,只不过是记录一下怎么取url中的参数的方法
    ##def get_object(self,queryset=None):
    ##    otrequest_id = int(self.kwargs.get(self.pk_url_kwarg, None))
    ##    otrequest = OtRequest.objects.get(id = otrequest_id)
    ##    return otrequest

    ##def get_context_data(self, **kwargs):
    ##    context = super().get_context_data(**kwargs)
    ##    return context

class OtRequestUpdateView(LoginRequiredMixin, UpdateView):
    login_url = "/account/login/"

    model = OtRequest
    template_name_suffix = '_update_form'
    success_url = reverse_lazy("otrest:list_otrequest")
    form_class = OtRequestForm
## 加班申请 结束
## ==================================================================================================

## 加班凭证 开始
class OtRecordCreateView(LoginRequiredMixin, CreateView):
    login_url = "/account/login/"
    template_name = 'otrest/layer_otrecord_create.html'
    fields = ['startTime', 'endTime', 'certPic']
    extra_context = {'m2':'active open', 'm2s2':'active'}

    model = OtRecord

    # get()里的参数必须加上 *args,**kwargs或者是url里传进来的key,可以写成 get(self, request, pk)也没错,但是不写就会报错
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        otrequest_id = int(self.kwargs.get(self.pk_url_kwarg, None))
        otrequest = OtRequest.objects.get(id = otrequest_id)  
        
        otrecord_form = OtRecordForm(request.POST)
        
        if otrecord_form.is_valid():
            form_cd = otrecord_form.cleaned_data
            new_otrecord = otrecord_form.save(commit=False)
            new_otrecord.certPic = request.FILES.get('certPic', None)
            new_otrecord.user = request.user
            new_otrecord.otrequest = otrequest
            new_otrecord.isCommit = True
            new_otrecord.save(form_cd)

        return redirect("otrest:list_otrequest")


class OtRecordListView(LoginRequiredMixin, TemplateView):
    login_url = "/account/login/"
    template_name = 'otrest/otrecord_list.html'
    extra_context = {'m2':'active open', 'm2s3':'active'}

    def get(self, request):
        return render(request, self.template_name, self.extra_context)

    def post(self, request, *args, **kwargs):
        page = request.POST.get('page')
        rows = request.POST.get('limit')

        i = (int(page) - 1) * int(rows)
        j = (int(page) - 1) * int(rows) + int(rows)

        otrecords = OtRecord.objects.filter(user = self.request.user)
        total = otrecords.count()

        otrecords = otrecords[i:j]

        dict = []
        resultdict = {}

        for r in otrecords:
            dic = {}
            dic['id'] = r.id
            dic['startTime'] = r.startTime.strftime("%Y-%m-%d %H:%M:%S")
            dic['endTime'] = r.endTime.strftime("%Y-%m-%d %H:%M:%S")
            dic['certPic'] = r.certPic.name
            dic['thumbCertPic'] = r.thumbCertPic.name
            dic['created'] = r.created.strftime("%Y-%m-%d %H:%M:%S")
            dict.append(dic)

        resultdict['code'] = 0
        resultdict['msg'] = ""
        resultdict['count'] = total 
        resultdict['data'] = dict

        return JsonResponse(resultdict, safe=False) 

## 加班凭证 结束
