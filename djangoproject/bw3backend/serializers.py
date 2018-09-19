from . import models

from rest_framework import serializers


class clientSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.client
        fields = (
            'pk', 
            'name', 
            'created', 
            'password', 
        )


class client_configSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.client_config
        fields = (
            'pk', 
            'setting', 
            'value', 
        )


class pluginSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.plugin
        fields = (
            'pk', 
            'name', 
            'version', 
            'builddate', 
            'creator', 
        )


class plugininstanceSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.plugininstance
        fields = (
            'pk', 
            'name', 
            'created', 
            'set_active', 
            'set_callbychild', 
            'set_calldirect', 
        )


class orga_unitsSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.orga_units
        fields = (
            'pk', 
            'name', 
            'description', 
            'optaname', 
        )


class orga_locationSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.orga_location
        fields = (
            'pk', 
            'name', 
            'addr_street', 
            'addr_nr', 
            'addr_plz', 
            'addr_city', 
            'telephone', 
        )


class orga_vehicalSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.orga_vehical
        fields = (
            'pk', 
            'name', 
            'optaname', 
            'numberplate', 
        )


class plugin_configSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.plugin_config
        fields = (
            'pk', 
            'setting', 
            'value', 
        )


class dataincomingSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.dataincoming
        fields = (
            'pk', 
            'created', 
            'cliententrytime', 
            'workload', 
            'direction', 
            'callid', 
        )


class helper_datatypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.helper_datatype
        fields = (
            'pk', 
            'name', 
        )


class plugininstance_configSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.plugininstance_config
        fields = (
            'pk', 
            'setting', 
            'value', 
        )


class globalconfigSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.globalconfig
        fields = (
            'pk', 
            'setting', 
            'value', 
        )


