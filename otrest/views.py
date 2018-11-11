from django.shortcuts import render, redirect
from braces.views import LoginRequiredMixin
from django.views.generic import CreateView, ListView, DeleteView, UpdateView
from django.views.generic.base import TemplateView
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.http import HttpResponse
import json

from .models import OtRequest
from .forms import OtRequestForm

# Create your views here.

class OtRequestView(LoginRequiredMixin, CreateView):
    login_url = "/account/login/"

    fields = ['ottime', 'reason']
    template_name = 'otrest/ot_request.html'

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

class OtRequestListView(LoginRequiredMixin, ListView):
    login_url = "/account/login/"
    model = OtRequest
    context_object_name = "otrequests"
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
    
class OtRequestUpdateView(LoginRequiredMixin, UpdateView):
    login_url = "/account/login/"
    template_name = "otrest/ot_request_edit.html"
    template_name_suffix = '_update_form'

    form_class = OtRequestForm
    model = OtRequest
    success_url = reverse_lazy("otrest:list_otrequest")
