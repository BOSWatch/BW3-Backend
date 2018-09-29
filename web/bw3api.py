import os
import django
from datetime import datetime

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bw3webinterface.settings')
django.setup()
from bw3backend import models as dmodels



# HIER WERDEEN GLOBALE KONFIGURATIONEN GEHOLT
class Global:

    def get_all_config():
        """Gets all Global Configurations
        @return QuerySet"""
        return dmodels.GlobalConfig.objects.all()

    def get_config(setting):
        """Gets specific Configuration
        @param setting: Name of the Setting
        @return String or 0 if not exisits"""
        opt = dmodels.GlobalConfig.objects.get(setting=setting)
        if opt is None:
            return 0
        return opt.value

# Hier werden Client-spezifische Konfigurationen geholt
class Client:

    def get_all_client():
        """Gets all Clients
        @return QuerySet"""
        return dmodels.Client.objects.all()

    def get_client(client):
        """Gets all Global Configurations
        @param [String]client : Clientname
        @return object"""
        return dmodels.Client.objects.get(name=client)

    def get_all_config(client):
        """Gets all Configurations of specific Client
        @param [Object]client
        @return Value"""
        opts = dmodels.Client_Config.objects.filter(client=client)
        return opts

    def get_config(client, setting):
        """Gets all Global Configurations
        @param [Object] client
        @param [String] Setting Name
        @return QuerySet"""
        opts = dmodels.Client_Config.objects.filter(client=client, setting=setting)
        return opts[0]

    def set_client_lastseen(client):
        """Set the LastSeen of a Client to now
        @param [object] Client
        @return True of False"""
        try:
            obj = dmodels.Client.object.get(name=client)
            obj.lastseen = datetime.now()
            obj.save()
            back = True
        except:
            back = False
        return back



# Alle Pluginkonfigurationen
class Plugin:

    def get_all():
        """Gets all Plugins
        @return QuerySet"""
        return dmodels.Plugin.objects.all()

    def get_plugin(plugin):
        """Gets a Plugin
        @param [String] Plugin
        @return Object"""
        return dmodels.Plugin.objects.get(name=plugin)

    def get_all_config():
        """Gets all Plugin Configurations
        @return QuerySet"""
        return dmodels.Plugin_Config.objects.all()


class Plugininst:
    def get_all_plugininst():
        return dmodels.PluginInstance.objects.all()

    def get_plugininst_by_plugin(plugin):
        return dmodels.PluginInstance.objects.filter(plugin=plugin)




class Orga:

    def get_all_units():
        return dmodels.Orga_Units.objects.all()


    def get_all_location():
        return dmodels.Orga_Location.objects.all()

    def get_all_vehicals():
        return dmodels.Orga_Vehical.objects.all()


    def get_unit_by_data(data):
        return dmodels.Orga_Units.objects.filter(data=data)

    def get_vehical_by_data(data):
        return dmodels.Orga_Vehical.objects.filter(data=data)

    def get_location_by_data(data):
        return dmodels.Orga_Location.objects.filter(data=data)


    def get_parents_by_data(data):
        origin = dmodels.Orga_Units.objects.filter(data=data)
        for obj in origin:
            output = output + origin.parent


class Data:

    def get_or_create_data(type, callid):
        try:
            obj = dmodels.Data.objects.get(callid=callid,type=type)
        except dmodels.Data.DoesNotExist:
            obj = dmodels.Data(callid=callid,type=type)
            obj.save()
            return obj
        return obj


