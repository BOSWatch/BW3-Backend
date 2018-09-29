# vim: set fileencoding=utf-8 :
from django.contrib import admin

from . import models


class Helper_DatatypeAdmin(admin.ModelAdmin):

    list_display = ('id', 'name')
    search_fields = ('name',)


class Helper_InputtypeAdmin(admin.ModelAdmin):

    list_display = ('id', 'name', 'value')
    search_fields = ('name',)


class DataAdmin(admin.ModelAdmin):

    list_display = ('id', 'direction', 'callid', 'type')
    list_filter = ('direction', 'type')


class ClientAdmin(admin.ModelAdmin):

    list_display = ('id', 'name', 'created', 'password', 'lastseen')
    list_filter = ('created', 'lastseen')
    search_fields = ('name',)


class Client_ConfigAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'order',
        'setting',
        'value',
        'front_name',
        'front_description',
        'pattern',
        'inputtype',
        'client',
    )
    list_filter = ('inputtype', 'client')


class PluginAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'name',
        'version',
        'builddate',
        'creator',
        'needsinternet',
        'front_name',
        'front_description',
    )
    list_filter = ('builddate', 'needsinternet')
    raw_id_fields = ('possibledatatypes',)
    search_fields = ('name',)


class PluginInstanceAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'front_name',
        'name',
        'created',
        'active',
        'plugin',
        'createdby',
    )
    list_filter = ('created', 'active', 'plugin', 'createdby')
    search_fields = ('name',)


class Orga_LocationAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'name',
        'addr_street',
        'addr_nr',
        'addr_plz',
        'addr_city',
        'telephone',
    )
    search_fields = ('name',)


class Orga_VehicalAdmin(admin.ModelAdmin):

    list_display = ('id', 'name', 'optaname', 'numberplate', 'fmskennung')
    list_filter = ('fmskennung',)
    search_fields = ('name',)


class Orga_UnitsAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'name',
        'description',
        'optaname',
        'inheritalarm',
        'location',
        'parent',
    )
    list_filter = ('inheritalarm', 'location', 'parent')
    raw_id_fields = ('vehicals',)
    search_fields = ('name',)


class Plugin_ConfigAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'order',
        'setting',
        'value',
        'front_name',
        'front_description',
        'pattern',
        'inputtype',
        'plugin',
    )
    list_filter = ('inputtype', 'plugin')


class DataIncomingAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'created',
        'cliententrytime',
        'workload',
        'direction',
        'callid',
        'client',
    )
    list_filter = (
        'created',
        'cliententrytime',
        'direction',
        'callid',
        'client',
    )


class PluginInstance_Config_TemplateAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'order',
        'setting',
        'default_value',
        'front_name',
        'front_description',
        'pattern',
        'inputtype',
        'plugin',
    )
    list_filter = ('inputtype', 'plugin')


class PluginInstance_ConfigAdmin(admin.ModelAdmin):

    list_display = ('id', 'value', 'plugininstance', 'template')
    list_filter = ('plugininstance', 'template')


class GlobalConfig_SectionAdmin(admin.ModelAdmin):

    list_display = ('id', 'order', 'front_name', 'front_description')


class GlobalConfigAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'order',
        'setting',
        'value',
        'front_name',
        'front_description',
        'pattern',
        'inputtype',
        'section',
    )
    list_filter = ('inputtype', 'section')


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Helper_Datatype, Helper_DatatypeAdmin)
_register(models.Helper_Inputtype, Helper_InputtypeAdmin)
_register(models.Data, DataAdmin)
_register(models.Client, ClientAdmin)
_register(models.Client_Config, Client_ConfigAdmin)
_register(models.Plugin, PluginAdmin)
_register(models.PluginInstance, PluginInstanceAdmin)
_register(models.Orga_Location, Orga_LocationAdmin)
_register(models.Orga_Vehical, Orga_VehicalAdmin)
_register(models.Orga_Units, Orga_UnitsAdmin)
_register(models.Plugin_Config, Plugin_ConfigAdmin)
_register(models.DataIncoming, DataIncomingAdmin)
_register(
    models.PluginInstance_Config_Template,
    PluginInstance_Config_TemplateAdmin)
_register(models.PluginInstance_Config, PluginInstance_ConfigAdmin)
_register(models.GlobalConfig_Section, GlobalConfig_SectionAdmin)
_register(models.GlobalConfig, GlobalConfigAdmin)
