from django.views.generic import DetailView, ListView, UpdateView, CreateView
from .models import client, client_config, plugin, plugininstance, orga_units, orga_location, orga_vehical, plugin_config, dataincoming, helper_datatype, plugininstance_config, globalconfig
from .forms import clientForm, client_configForm, pluginForm, plugininstanceForm, orga_unitsForm, orga_locationForm, orga_vehicalForm, plugin_configForm, dataincomingForm, helper_datatypeForm, plugininstance_configForm, globalconfigForm


class clientListView(ListView):
    model = client


class clientCreateView(CreateView):
    model = client
    form_class = clientForm


class clientDetailView(DetailView):
    model = client


class clientUpdateView(UpdateView):
    model = client
    form_class = clientForm


class client_configListView(ListView):
    model = client_config


class client_configCreateView(CreateView):
    model = client_config
    form_class = client_configForm


class client_configDetailView(DetailView):
    model = client_config


class client_configUpdateView(UpdateView):
    model = client_config
    form_class = client_configForm


class pluginListView(ListView):
    model = plugin


class pluginCreateView(CreateView):
    model = plugin
    form_class = pluginForm


class pluginDetailView(DetailView):
    model = plugin


class pluginUpdateView(UpdateView):
    model = plugin
    form_class = pluginForm


class plugininstanceListView(ListView):
    model = plugininstance


class plugininstanceCreateView(CreateView):
    model = plugininstance
    form_class = plugininstanceForm


class plugininstanceDetailView(DetailView):
    model = plugininstance


class plugininstanceUpdateView(UpdateView):
    model = plugininstance
    form_class = plugininstanceForm


class orga_unitsListView(ListView):
    model = orga_units


class orga_unitsCreateView(CreateView):
    model = orga_units
    form_class = orga_unitsForm


class orga_unitsDetailView(DetailView):
    model = orga_units


class orga_unitsUpdateView(UpdateView):
    model = orga_units
    form_class = orga_unitsForm


class orga_locationListView(ListView):
    model = orga_location


class orga_locationCreateView(CreateView):
    model = orga_location
    form_class = orga_locationForm


class orga_locationDetailView(DetailView):
    model = orga_location


class orga_locationUpdateView(UpdateView):
    model = orga_location
    form_class = orga_locationForm


class orga_vehicalListView(ListView):
    model = orga_vehical


class orga_vehicalCreateView(CreateView):
    model = orga_vehical
    form_class = orga_vehicalForm


class orga_vehicalDetailView(DetailView):
    model = orga_vehical


class orga_vehicalUpdateView(UpdateView):
    model = orga_vehical
    form_class = orga_vehicalForm


class plugin_configListView(ListView):
    model = plugin_config


class plugin_configCreateView(CreateView):
    model = plugin_config
    form_class = plugin_configForm


class plugin_configDetailView(DetailView):
    model = plugin_config


class plugin_configUpdateView(UpdateView):
    model = plugin_config
    form_class = plugin_configForm


class dataincomingListView(ListView):
    model = dataincoming


class dataincomingCreateView(CreateView):
    model = dataincoming
    form_class = dataincomingForm


class dataincomingDetailView(DetailView):
    model = dataincoming


class dataincomingUpdateView(UpdateView):
    model = dataincoming
    form_class = dataincomingForm


class helper_datatypeListView(ListView):
    model = helper_datatype


class helper_datatypeCreateView(CreateView):
    model = helper_datatype
    form_class = helper_datatypeForm


class helper_datatypeDetailView(DetailView):
    model = helper_datatype


class helper_datatypeUpdateView(UpdateView):
    model = helper_datatype
    form_class = helper_datatypeForm


class plugininstance_configListView(ListView):
    model = plugininstance_config


class plugininstance_configCreateView(CreateView):
    model = plugininstance_config
    form_class = plugininstance_configForm


class plugininstance_configDetailView(DetailView):
    model = plugininstance_config


class plugininstance_configUpdateView(UpdateView):
    model = plugininstance_config
    form_class = plugininstance_configForm


class globalconfigListView(ListView):
    model = globalconfig


class globalconfigCreateView(CreateView):
    model = globalconfig
    form_class = globalconfigForm


class globalconfigDetailView(DetailView):
    model = globalconfig


class globalconfigUpdateView(UpdateView):
    model = globalconfig
    form_class = globalconfigForm

