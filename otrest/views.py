from django.shortcuts import render, redirect
from braces.views import LoginRequiredMixin
from django.views.generic import CreateView, ListView, DeleteView, UpdateView, DetailView
from django.views.generic.base import TemplateView
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.http import HttpResponse
import json

from .models import OtRequest
from .forms import OtRequestForm

# Create your views here.

class OtRequestCreateView(LoginRequiredMixin, CreateView):
    login_url = "/account/login/"
    fields = ['ottime', 'reason']
    template_name = 'otrest/ot_request.html'
    extra_context = {'class_open':'active open', 'class_active':'active'}

    ##Note1 当继承的是TempLateView时使用这个
    ##def get(self, request):
    ##    return render(request, "otrest/ot_request.html")
    
    ##Note2 当继承的是CreateView时使用这个,功能与Note1是一样的,只是两种不同的实现方式
    queryset = OtRequest.objects.all()

    def post(self, request, *args, **kwargs):
        user = User.objects.get(username = request.user.username)
        otrequest_form = OtRequestForm(request.POST)

        if otrequest_form.is_valid():
            form_cd = otrequest_form.cleaned_data 
            new_otrequest = otrequest_form.save(commit=False)
            new_otrequest.user = request.user
            new_otrequest.save(form_cd)
            return redirect("otrest:list_otrequest")
        return self.render_to_response({"form":otrequest_form})

class OtRequestListView(LoginRequiredMixin, ListView):
    login_url = "/account/login/"
    model = OtRequest
    context_object_name = "otrequests"
    extra_context = {'class_open':'active open', 'class_active':'active'}
    template_name = 'otrest/ot_request_list.html'

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
    template_name = "otrest/ot_request_edit.html"
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
