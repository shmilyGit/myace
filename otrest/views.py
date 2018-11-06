from django.shortcuts import render, redirect
from braces.views import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.views.generic.base import TemplateView
from django.contrib.auth.models import User

from .models import OtRequest
from .forms import OtRequestForm
# Create your views here.

class OtRequestView(LoginRequiredMixin, TemplateView):
    login_url = "/account/login/"

    fields = ['ottime', 'reason']
    template_name = 'otrest/ot_request.html'

    def get(self, request):
        return render(request, "otrest/ot_request.html")

    def post(self, request, *args, **kwargs):
        user = User.objects.get(username = request.user.username)
        otrequest_form = OtRequestForm(request.POST)

        if otrequest_form.is_valid():
            form_cd = otrequest_form.cleaned_data 
            print ("==============================1", form_cd)
            new_otrequest = otrequest_form.save(commit=False)
            new_otrequest.user = request.user
            new_otrequest.save(form_cd)
            return redirect("otrest:ot_request")

