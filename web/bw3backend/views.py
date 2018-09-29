from django.views.generic import DetailView, ListView, UpdateView, CreateView
from .models import *
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect



def Einstellungen(request):
  #  if not request.user.is_authenticated:
   #     return redirect('%s?next=%s' % ("/accounts/login", request.path))
    all_global_config_list = Client_Config.objects.all()
    template = loader.get_template('Einstellungen.html')
    context = {
        'all_global_config_list': all_global_config_list,
    }
    return HttpResponse(template.render(context, request))



