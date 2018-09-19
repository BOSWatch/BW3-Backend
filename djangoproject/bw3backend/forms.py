from django import forms
from .models import client, client_config, plugin, plugininstance, orga_units, orga_location, orga_vehical, plugin_config, dataincoming, helper_datatype, plugininstance_config, globalconfig


class clientForm(forms.ModelForm):
    class Meta:
        model = client
        fields = ['name', 'password']


class client_configForm(forms.ModelForm):
    class Meta:
        model = client_config
        fields = ['setting', 'value', 'client']


class pluginForm(forms.ModelForm):
    class Meta:
        model = plugin
        fields = ['name', 'version', 'builddate', 'creator']


class plugininstanceForm(forms.ModelForm):
    class Meta:
        model = plugininstance
        fields = ['name', 'set_active', 'set_callbychild', 'set_calldirect', 'plugin', 'createdby']


class orga_unitsForm(forms.ModelForm):
    class Meta:
        model = orga_units
        fields = ['name', 'description', 'optaname', 'location', 'vehicals', 'parent']


class orga_locationForm(forms.ModelForm):
    class Meta:
        model = orga_location
        fields = ['name', 'addr_street', 'addr_nr', 'addr_plz', 'addr_city', 'telephone']


class orga_vehicalForm(forms.ModelForm):
    class Meta:
        model = orga_vehical
        fields = ['name', 'optaname', 'numberplate', 'fmskennung', 'location']


class plugin_configForm(forms.ModelForm):
    class Meta:
        model = plugin_config
        fields = ['setting', 'value', 'plugin']


class dataincomingForm(forms.ModelForm):
    class Meta:
        model = dataincoming
        fields = ['cliententrytime', 'workload', 'direction', 'callid', 'client', 'type']


class helper_datatypeForm(forms.ModelForm):
    class Meta:
        model = helper_datatype
        fields = ['name']


class plugininstance_configForm(forms.ModelForm):
    class Meta:
        model = plugininstance_config
        fields = ['setting', 'value', 'plugininstance']


class globalconfigForm(forms.ModelForm):
    class Meta:
        model = globalconfig
        fields = ['setting', 'value']


