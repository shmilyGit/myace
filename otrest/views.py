from django.shortcuts import render
from braces.views import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.views.generic.base import TemplateView

from .forms import OtRestForm
from .models import OtRest
# Create your views here.

class OtRestView(LoginRequiredMixin, TemplateView):
    login_url = "/account/login/"

    fields = ['ottime', 'reason']
    template_name = 'otrest/ot_request.html'

    def get(self, request):
        return render(request, "otrest/ot_request.html")

