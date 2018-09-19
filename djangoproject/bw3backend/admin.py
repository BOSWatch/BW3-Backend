from django.contrib import admin
from django import forms
from .models import client, client_config, plugin, plugininstance, orga_units, orga_location, orga_vehical, plugin_config, dataincoming, helper_datatype, plugininstance_config, globalconfig, data

class clientAdminForm(forms.ModelForm):

    class Meta:
        model = client
        fields = '__all__'


class clientAdmin(admin.ModelAdmin):
    form = clientAdminForm
    list_display = ['name', 'created', 'password']


admin.site.register(client, clientAdmin)


class client_configAdminForm(forms.ModelForm):

    class Meta:
        model = client_config
        fields = '__all__'


class client_configAdmin(admin.ModelAdmin):
    form = clientAdminForm
    list_display = ['setting', 'value', 'client']
	
	
admin.site.register(client_config, client_configAdmin)


class pluginAdminForm(forms.ModelForm):

    class Meta:
        model = plugin
        fields = '__all__'


class pluginAdmin(admin.ModelAdmin):
    form = pluginAdminForm
    list_display = ['name', 'version', 'builddate', 'creator']
	

	

admin.site.register(plugin, pluginAdmin)

class plugin_configAdminForm(forms.ModelForm):

    class Meta:
        model = plugin_config
        fields = '__all__'


class plugin_configAdmin(admin.ModelAdmin):
    form = plugin_configAdminForm
    list_display = ['setting', 'value', 'plugin']
	


admin.site.register(plugin_config, plugin_configAdmin)


class plugininstanceAdminForm(forms.ModelForm):

    class Meta:
        model = plugininstance
        fields = '__all__'


class plugininstanceAdmin(admin.ModelAdmin):
    form = plugininstanceAdminForm
    list_display = ['name', 'plugin', 'createdby' , 'set_active', 'set_callbychild', 'set_calldirect']


admin.site.register(plugininstance,plugininstanceAdmin)


class plugininstance_configAdminForm(forms.ModelForm):

    class Meta:
        model = plugininstance_config
        fields = '__all__'


class plugininstance_configAdmin(admin.ModelAdmin):
    form = plugininstance_configAdminForm
    list_display = ['setting', 'value', 'plugininstance']




admin.site.register(plugininstance_config,plugininstance_configAdmin)

class orga_locationAdminForm(forms.ModelForm):

    class Meta:
        model = orga_location
        fields = '__all__'


class orga_locationAdmin(admin.ModelAdmin):
    form = orga_locationAdminForm
    list_display = ['name', 'addr_street', 'addr_nr', 'addr_plz', 'addr_city', 'telephone']



admin.site.register(orga_location, orga_locationAdmin)


class orga_unitsAdminForm(forms.ModelForm):

    class Meta:
        model = orga_units
        fields = '__all__'


class orga_unitsAdmin(admin.ModelAdmin):
    form = orga_unitsAdminForm
    list_display = ['name', 'description', 'optaname', 'location' ,'parent']



admin.site.register(orga_units, orga_unitsAdmin)

class orga_vehicalAdminForm(forms.ModelForm):

    class Meta:
        model = orga_vehical
        fields = '__all__'


class orga_vehicalAdmin(admin.ModelAdmin):
    form = orga_vehicalAdminForm
    list_display = ['optaname', 'fmskennung', 'location']



admin.site.register(orga_vehical, orga_vehicalAdmin)


class dataincomingAdminForm(forms.ModelForm):

    class Meta:
        model = dataincoming
        fields = '__all__'


class dataincomingAdmin(admin.ModelAdmin):
    form = dataincomingAdminForm
    list_display = ['workload', 'callid', 'cliententrytime']


admin.site.register(dataincoming, dataincomingAdmin)

class dataAdminForm(forms.ModelForm):

    class Meta:
        model = data
        fields = '__all__'


class dataAdmin(admin.ModelAdmin):
    form = dataAdminForm
    list_display = ['callid', 'type']


admin.site.register(data, dataAdmin)

class helper_datatypeAdminForm(forms.ModelForm):

    class Meta:
        model = helper_datatype
        fields = '__all__'


class helper_datatypeAdmin(admin.ModelAdmin):
    form = helper_datatypeAdminForm
    list_display = ['name']



admin.site.register(helper_datatype, helper_datatypeAdmin)

class globalconfigAdminForm(forms.ModelForm):

    class Meta:
        model = globalconfig
        fields = '__all__'


class globalconfigAdmin(admin.ModelAdmin):
    form = globalconfigAdminForm
    list_display = ['setting', 'value']

admin.site.register(globalconfig, globalconfigAdmin)