import unittest
from django.urls import reverse
from django.test import Client
from .models import client, client_config, plugin, plugininstance, orga_units, orga_location, orga_vehical, plugin_config, dataincoming, helper_datatype, plugininstance_config, globalconfig
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.contrib.contenttypes.models import ContentType


def create_django_contrib_auth_models_user(**kwargs):
    defaults = {}
    defaults["username"] = "username"
    defaults["email"] = "username@tempurl.com"
    defaults.update(**kwargs)
    return User.objects.create(**defaults)


def create_django_contrib_auth_models_group(**kwargs):
    defaults = {}
    defaults["name"] = "group"
    defaults.update(**kwargs)
    return Group.objects.create(**defaults)


def create_django_contrib_contenttypes_models_contenttype(**kwargs):
    defaults = {}
    defaults.update(**kwargs)
    return ContentType.objects.create(**defaults)


def create_client(**kwargs):
    defaults = {}
    defaults["name"] = "name"
    defaults["password"] = "password"
    defaults.update(**kwargs)
    return client.objects.create(**defaults)


def create_client_config(**kwargs):
    defaults = {}
    defaults["setting"] = "setting"
    defaults["value"] = "value"
    defaults.update(**kwargs)
    if "client" not in defaults:
        defaults["client"] = create_global_client()
    return client_config.objects.create(**defaults)


def create_plugin(**kwargs):
    defaults = {}
    defaults["name"] = "name"
    defaults["version"] = "version"
    defaults["builddate"] = "builddate"
    defaults["creator"] = "creator"
    defaults.update(**kwargs)
    return plugin.objects.create(**defaults)


def create_plugininstance(**kwargs):
    defaults = {}
    defaults["name"] = "name"
    defaults["set_active"] = "set_active"
    defaults["set_callbychild"] = "set_callbychild"
    defaults["set_calldirect"] = "set_calldirect"
    defaults.update(**kwargs)
    if "plugin" not in defaults:
        defaults["plugin"] = create_plugin()
    if "createdby" not in defaults:
        defaults["createdby"] = create_django_contrib_auth_models_user()
    return plugininstance.objects.create(**defaults)


def create_orga_units(**kwargs):
    defaults = {}
    defaults["name"] = "name"
    defaults["description"] = "description"
    defaults["optaname"] = "optaname"
    defaults.update(**kwargs)
    if "location" not in defaults:
        defaults["location"] = create_orga_location()
    if "vehicals" not in defaults:
        defaults["vehicals"] = create_django_contrib_auth_models_user()
    if "parent" not in defaults:
        defaults["parent"] = create_orga_units()
    return orga_units.objects.create(**defaults)


def create_orga_location(**kwargs):
    defaults = {}
    defaults["name"] = "name"
    defaults["addr_street"] = "addr_street"
    defaults["addr_nr"] = "addr_nr"
    defaults["addr_plz"] = "addr_plz"
    defaults["addr_city"] = "addr_city"
    defaults["telephone"] = "telephone"
    defaults.update(**kwargs)
    return orga_location.objects.create(**defaults)


def create_orga_vehical(**kwargs):
    defaults = {}
    defaults["name"] = "name"
    defaults["optaname"] = "optaname"
    defaults["numberplate"] = "numberplate"
    defaults.update(**kwargs)
    if "fmskennung" not in defaults:
        defaults["fmskennung"] = create_data_fms()
    if "location" not in defaults:
        defaults["location"] = create_orga_location()
    return orga_vehical.objects.create(**defaults)


def create_plugin_config(**kwargs):
    defaults = {}
    defaults["setting"] = "setting"
    defaults["value"] = "value"
    defaults.update(**kwargs)
    if "plugin" not in defaults:
        defaults["plugin"] = create_plugin()
    return plugin_config.objects.create(**defaults)


def create_dataincoming(**kwargs):
    defaults = {}
    defaults["cliententrytime"] = "cliententrytime"
    defaults["workload"] = "workload"
    defaults["direction"] = "direction"
    defaults["callid"] = "callid"
    defaults.update(**kwargs)
    if "client" not in defaults:
        defaults["client"] = create_client()
    if "type" not in defaults:
        defaults["type"] = create_helper_datatype()
    return dataincoming.objects.create(**defaults)


def create_helper_datatype(**kwargs):
    defaults = {}
    defaults["name"] = "name"
    defaults.update(**kwargs)
    return helper_datatype.objects.create(**defaults)


def create_plugininstance_config(**kwargs):
    defaults = {}
    defaults["setting"] = "setting"
    defaults["value"] = "value"
    defaults.update(**kwargs)
    if "plugininstance" not in defaults:
        defaults["plugininstance"] = create_plugininstance()
    return plugininstance_config.objects.create(**defaults)


def create_globalconfig(**kwargs):
    defaults = {}
    defaults["setting"] = "setting"
    defaults["value"] = "value"
    defaults.update(**kwargs)
    return globalconfig.objects.create(**defaults)


class clientViewTest(unittest.TestCase):
    '''
    Tests for client
    '''
    def setUp(self):
        self.client = Client()

    def test_list_client(self):
        url = reverse('bw3backend_client_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_client(self):
        url = reverse('bw3backend_client_create')
        data = {
            "name": "name",
            "password": "password",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_client(self):
        client = create_client()
        url = reverse('bw3backend_client_detail', args=[client.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_client(self):
        client = create_client()
        data = {
            "name": "name",
            "password": "password",
        }
        url = reverse('bw3backend_client_update', args=[client.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class client_configViewTest(unittest.TestCase):
    '''
    Tests for client_config
    '''
    def setUp(self):
        self.client = Client()

    def test_list_client_config(self):
        url = reverse('bw3backend_client_config_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_client_config(self):
        url = reverse('bw3backend_client_config_create')
        data = {
            "setting": "setting",
            "value": "value",
            "client": create_global_client().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_client_config(self):
        client_config = create_client_config()
        url = reverse('bw3backend_client_config_detail', args=[client_config.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_client_config(self):
        client_config = create_client_config()
        data = {
            "setting": "setting",
            "value": "value",
            "client": create_global_client().pk,
        }
        url = reverse('bw3backend_client_config_update', args=[client_config.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class pluginViewTest(unittest.TestCase):
    '''
    Tests for plugin
    '''
    def setUp(self):
        self.client = Client()

    def test_list_plugin(self):
        url = reverse('bw3backend_plugin_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_plugin(self):
        url = reverse('bw3backend_plugin_create')
        data = {
            "name": "name",
            "version": "version",
            "builddate": "builddate",
            "creator": "creator",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_plugin(self):
        plugin = create_plugin()
        url = reverse('bw3backend_plugin_detail', args=[plugin.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_plugin(self):
        plugin = create_plugin()
        data = {
            "name": "name",
            "version": "version",
            "builddate": "builddate",
            "creator": "creator",
        }
        url = reverse('bw3backend_plugin_update', args=[plugin.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class plugininstanceViewTest(unittest.TestCase):
    '''
    Tests for plugininstance
    '''
    def setUp(self):
        self.client = Client()

    def test_list_plugininstance(self):
        url = reverse('bw3backend_plugininstance_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_plugininstance(self):
        url = reverse('bw3backend_plugininstance_create')
        data = {
            "name": "name",
            "set_active": "set_active",
            "set_callbychild": "set_callbychild",
            "set_calldirect": "set_calldirect",
            "plugin": create_plugin().pk,
            "createdby": create_django_contrib_auth_models_user().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_plugininstance(self):
        plugininstance = create_plugininstance()
        url = reverse('bw3backend_plugininstance_detail', args=[plugininstance.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_plugininstance(self):
        plugininstance = create_plugininstance()
        data = {
            "name": "name",
            "set_active": "set_active",
            "set_callbychild": "set_callbychild",
            "set_calldirect": "set_calldirect",
            "plugin": create_plugin().pk,
            "createdby": create_django_contrib_auth_models_user().pk,
        }
        url = reverse('bw3backend_plugininstance_update', args=[plugininstance.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class orga_unitsViewTest(unittest.TestCase):
    '''
    Tests for orga_units
    '''
    def setUp(self):
        self.client = Client()

    def test_list_orga_units(self):
        url = reverse('bw3backend_orga_units_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_orga_units(self):
        url = reverse('bw3backend_orga_units_create')
        data = {
            "name": "name",
            "description": "description",
            "optaname": "optaname",
            "location": create_orga_location().pk,
            "vehicals": create_django_contrib_auth_models_user().pk,
            "parent": create_orga_units().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_orga_units(self):
        orga_units = create_orga_units()
        url = reverse('bw3backend_orga_units_detail', args=[orga_units.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_orga_units(self):
        orga_units = create_orga_units()
        data = {
            "name": "name",
            "description": "description",
            "optaname": "optaname",
            "location": create_orga_location().pk,
            "vehicals": create_django_contrib_auth_models_user().pk,
            "parent": create_orga_units().pk,
        }
        url = reverse('bw3backend_orga_units_update', args=[orga_units.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class orga_locationViewTest(unittest.TestCase):
    '''
    Tests for orga_location
    '''
    def setUp(self):
        self.client = Client()

    def test_list_orga_location(self):
        url = reverse('bw3backend_orga_location_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_orga_location(self):
        url = reverse('bw3backend_orga_location_create')
        data = {
            "name": "name",
            "addr_street": "addr_street",
            "addr_nr": "addr_nr",
            "addr_plz": "addr_plz",
            "addr_city": "addr_city",
            "telephone": "telephone",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_orga_location(self):
        orga_location = create_orga_location()
        url = reverse('bw3backend_orga_location_detail', args=[orga_location.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_orga_location(self):
        orga_location = create_orga_location()
        data = {
            "name": "name",
            "addr_street": "addr_street",
            "addr_nr": "addr_nr",
            "addr_plz": "addr_plz",
            "addr_city": "addr_city",
            "telephone": "telephone",
        }
        url = reverse('bw3backend_orga_location_update', args=[orga_location.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class orga_vehicalViewTest(unittest.TestCase):
    '''
    Tests for orga_vehical
    '''
    def setUp(self):
        self.client = Client()

    def test_list_orga_vehical(self):
        url = reverse('bw3backend_orga_vehical_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_orga_vehical(self):
        url = reverse('bw3backend_orga_vehical_create')
        data = {
            "name": "name",
            "optaname": "optaname",
            "numberplate": "numberplate",
            "fmskennung": create_data_fms().pk,
            "location": create_orga_location().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_orga_vehical(self):
        orga_vehical = create_orga_vehical()
        url = reverse('bw3backend_orga_vehical_detail', args=[orga_vehical.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_orga_vehical(self):
        orga_vehical = create_orga_vehical()
        data = {
            "name": "name",
            "optaname": "optaname",
            "numberplate": "numberplate",
            "fmskennung": create_data_fms().pk,
            "location": create_orga_location().pk,
        }
        url = reverse('bw3backend_orga_vehical_update', args=[orga_vehical.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class plugin_configViewTest(unittest.TestCase):
    '''
    Tests for plugin_config
    '''
    def setUp(self):
        self.client = Client()

    def test_list_plugin_config(self):
        url = reverse('bw3backend_plugin_config_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_plugin_config(self):
        url = reverse('bw3backend_plugin_config_create')
        data = {
            "setting": "setting",
            "value": "value",
            "plugin": create_plugin().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_plugin_config(self):
        plugin_config = create_plugin_config()
        url = reverse('bw3backend_plugin_config_detail', args=[plugin_config.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_plugin_config(self):
        plugin_config = create_plugin_config()
        data = {
            "setting": "setting",
            "value": "value",
            "plugin": create_plugin().pk,
        }
        url = reverse('bw3backend_plugin_config_update', args=[plugin_config.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class dataincomingViewTest(unittest.TestCase):
    '''
    Tests for dataincoming
    '''
    def setUp(self):
        self.client = Client()

    def test_list_dataincoming(self):
        url = reverse('bw3backend_dataincoming_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_dataincoming(self):
        url = reverse('bw3backend_dataincoming_create')
        data = {
            "cliententrytime": "cliententrytime",
            "workload": "workload",
            "direction": "direction",
            "callid": "callid",
            "client": create_client().pk,
            "type": create_helper_datatype().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_dataincoming(self):
        dataincoming = create_dataincoming()
        url = reverse('bw3backend_dataincoming_detail', args=[dataincoming.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_dataincoming(self):
        dataincoming = create_dataincoming()
        data = {
            "cliententrytime": "cliententrytime",
            "workload": "workload",
            "direction": "direction",
            "callid": "callid",
            "client": create_client().pk,
            "type": create_helper_datatype().pk,
        }
        url = reverse('bw3backend_dataincoming_update', args=[dataincoming.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class helper_datatypeViewTest(unittest.TestCase):
    '''
    Tests for helper_datatype
    '''
    def setUp(self):
        self.client = Client()

    def test_list_helper_datatype(self):
        url = reverse('bw3backend_helper_datatype_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_helper_datatype(self):
        url = reverse('bw3backend_helper_datatype_create')
        data = {
            "name": "name",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_helper_datatype(self):
        helper_datatype = create_helper_datatype()
        url = reverse('bw3backend_helper_datatype_detail', args=[helper_datatype.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_helper_datatype(self):
        helper_datatype = create_helper_datatype()
        data = {
            "name": "name",
        }
        url = reverse('bw3backend_helper_datatype_update', args=[helper_datatype.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class plugininstance_configViewTest(unittest.TestCase):
    '''
    Tests for plugininstance_config
    '''
    def setUp(self):
        self.client = Client()

    def test_list_plugininstance_config(self):
        url = reverse('bw3backend_plugininstance_config_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_plugininstance_config(self):
        url = reverse('bw3backend_plugininstance_config_create')
        data = {
            "setting": "setting",
            "value": "value",
            "plugininstance": create_plugininstance().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_plugininstance_config(self):
        plugininstance_config = create_plugininstance_config()
        url = reverse('bw3backend_plugininstance_config_detail', args=[plugininstance_config.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_plugininstance_config(self):
        plugininstance_config = create_plugininstance_config()
        data = {
            "setting": "setting",
            "value": "value",
            "plugininstance": create_plugininstance().pk,
        }
        url = reverse('bw3backend_plugininstance_config_update', args=[plugininstance_config.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class globalconfigViewTest(unittest.TestCase):
    '''
    Tests for globalconfig
    '''
    def setUp(self):
        self.client = Client()

    def test_list_globalconfig(self):
        url = reverse('bw3backend_globalconfig_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_globalconfig(self):
        url = reverse('bw3backend_globalconfig_create')
        data = {
            "setting": "setting",
            "value": "value",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_globalconfig(self):
        globalconfig = create_globalconfig()
        url = reverse('bw3backend_globalconfig_detail', args=[globalconfig.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_globalconfig(self):
        globalconfig = create_globalconfig()
        data = {
            "setting": "setting",
            "value": "value",
        }
        url = reverse('bw3backend_globalconfig_update', args=[globalconfig.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


