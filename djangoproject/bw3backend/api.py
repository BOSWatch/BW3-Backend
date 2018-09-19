from . import models
from . import serializers
from rest_framework import viewsets, permissions


class clientViewSet(viewsets.ModelViewSet):
    """ViewSet for the client class"""

    queryset = models.client.objects.all()
    serializer_class = serializers.clientSerializer
    permission_classes = [permissions.IsAuthenticated]


class client_configViewSet(viewsets.ModelViewSet):
    """ViewSet for the client_config class"""

    queryset = models.client_config.objects.all()
    serializer_class = serializers.client_configSerializer
    permission_classes = [permissions.IsAuthenticated]


class pluginViewSet(viewsets.ModelViewSet):
    """ViewSet for the plugin class"""

    queryset = models.plugin.objects.all()
    serializer_class = serializers.pluginSerializer
    permission_classes = [permissions.IsAuthenticated]


class plugininstanceViewSet(viewsets.ModelViewSet):
    """ViewSet for the plugininstance class"""

    queryset = models.plugininstance.objects.all()
    serializer_class = serializers.plugininstanceSerializer
    permission_classes = [permissions.IsAuthenticated]


class orga_unitsViewSet(viewsets.ModelViewSet):
    """ViewSet for the orga_units class"""

    queryset = models.orga_units.objects.all()
    serializer_class = serializers.orga_unitsSerializer
    permission_classes = [permissions.IsAuthenticated]


class orga_locationViewSet(viewsets.ModelViewSet):
    """ViewSet for the orga_location class"""

    queryset = models.orga_location.objects.all()
    serializer_class = serializers.orga_locationSerializer
    permission_classes = [permissions.IsAuthenticated]


class orga_vehicalViewSet(viewsets.ModelViewSet):
    """ViewSet for the orga_vehical class"""

    queryset = models.orga_vehical.objects.all()
    serializer_class = serializers.orga_vehicalSerializer
    permission_classes = [permissions.IsAuthenticated]


class plugin_configViewSet(viewsets.ModelViewSet):
    """ViewSet for the plugin_config class"""

    queryset = models.plugin_config.objects.all()
    serializer_class = serializers.plugin_configSerializer
    permission_classes = [permissions.IsAuthenticated]


class dataincomingViewSet(viewsets.ModelViewSet):
    """ViewSet for the dataincoming class"""

    queryset = models.dataincoming.objects.all()
    serializer_class = serializers.dataincomingSerializer
    permission_classes = [permissions.IsAuthenticated]


class helper_datatypeViewSet(viewsets.ModelViewSet):
    """ViewSet for the helper_datatype class"""

    queryset = models.helper_datatype.objects.all()
    serializer_class = serializers.helper_datatypeSerializer
    permission_classes = [permissions.IsAuthenticated]


class plugininstance_configViewSet(viewsets.ModelViewSet):
    """ViewSet for the plugininstance_config class"""

    queryset = models.plugininstance_config.objects.all()
    serializer_class = serializers.plugininstance_configSerializer
    permission_classes = [permissions.IsAuthenticated]


class globalconfigViewSet(viewsets.ModelViewSet):
    """ViewSet for the globalconfig class"""

    queryset = models.globalconfig.objects.all()
    serializer_class = serializers.globalconfigSerializer
    permission_classes = [permissions.IsAuthenticated]


