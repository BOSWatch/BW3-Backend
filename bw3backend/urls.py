from django.urls import path, include
from rest_framework import routers

from . import api
from . import views

router = routers.DefaultRouter()
router.register(r'client', api.clientViewSet)
router.register(r'client_config', api.client_configViewSet)
router.register(r'plugin', api.pluginViewSet)
router.register(r'plugininstance', api.plugininstanceViewSet)
router.register(r'orga_units', api.orga_unitsViewSet)
router.register(r'orga_location', api.orga_locationViewSet)
router.register(r'orga_vehical', api.orga_vehicalViewSet)
router.register(r'plugin_config', api.plugin_configViewSet)
router.register(r'dataincoming', api.dataincomingViewSet)
router.register(r'helper_datatype', api.helper_datatypeViewSet)
router.register(r'plugininstance_config', api.plugininstance_configViewSet)
router.register(r'globalconfig', api.globalconfigViewSet)


urlpatterns = (
    path('index' , views.index),
    # urls for Django Rest Framework API
    path('api/v1/', include(router.urls)),
)

urlpatterns += (
    # urls for client
    path('bw3backend/client/', views.clientListView.as_view(), name='bw3backend_client_list'),
    path('bw3backend/client/create/', views.clientCreateView.as_view(), name='bw3backend_client_create'),
    path('bw3backend/client/detail/<int:pk>/', views.clientDetailView.as_view(), name='bw3backend_client_detail'),
    path('bw3backend/client/update/<int:pk>/', views.clientUpdateView.as_view(), name='bw3backend_client_update'),
)

urlpatterns += (
    # urls for client_config
    path('bw3backend/client_config/', views.client_configListView.as_view(), name='bw3backend_client_config_list'),
    path('bw3backend/client_config/create/', views.client_configCreateView.as_view(), name='bw3backend_client_config_create'),
    path('bw3backend/client_config/detail/<int:pk>/', views.client_configDetailView.as_view(), name='bw3backend_client_config_detail'),
    path('bw3backend/client_config/update/<int:pk>/', views.client_configUpdateView.as_view(), name='bw3backend_client_config_update'),
)

urlpatterns += (
    # urls for plugin
    path('bw3backend/plugin/', views.pluginListView.as_view(), name='bw3backend_plugin_list'),
    path('bw3backend/plugin/create/', views.pluginCreateView.as_view(), name='bw3backend_plugin_create'),
    path('bw3backend/plugin/detail/<int:pk>/', views.pluginDetailView.as_view(), name='bw3backend_plugin_detail'),
    path('bw3backend/plugin/update/<int:pk>/', views.pluginUpdateView.as_view(), name='bw3backend_plugin_update'),
)

urlpatterns += (
    # urls for plugininstance
    path('bw3backend/plugininstance/', views.plugininstanceListView.as_view(), name='bw3backend_plugininstance_list'),
    path('bw3backend/plugininstance/create/', views.plugininstanceCreateView.as_view(), name='bw3backend_plugininstance_create'),
    path('bw3backend/plugininstance/detail/<int:pk>/', views.plugininstanceDetailView.as_view(), name='bw3backend_plugininstance_detail'),
    path('bw3backend/plugininstance/update/<int:pk>/', views.plugininstanceUpdateView.as_view(), name='bw3backend_plugininstance_update'),
)

urlpatterns += (
    # urls for orga_units
    path('bw3backend/orga_units/', views.orga_unitsListView.as_view(), name='bw3backend_orga_units_list'),
    path('bw3backend/orga_units/create/', views.orga_unitsCreateView.as_view(), name='bw3backend_orga_units_create'),
    path('bw3backend/orga_units/detail/<int:pk>/', views.orga_unitsDetailView.as_view(), name='bw3backend_orga_units_detail'),
    path('bw3backend/orga_units/update/<int:pk>/', views.orga_unitsUpdateView.as_view(), name='bw3backend_orga_units_update'),
)

urlpatterns += (
    # urls for orga_location
    path('bw3backend/orga_location/', views.orga_locationListView.as_view(), name='bw3backend_orga_location_list'),
    path('bw3backend/orga_location/create/', views.orga_locationCreateView.as_view(), name='bw3backend_orga_location_create'),
    path('bw3backend/orga_location/detail/<int:pk>/', views.orga_locationDetailView.as_view(), name='bw3backend_orga_location_detail'),
    path('bw3backend/orga_location/update/<int:pk>/', views.orga_locationUpdateView.as_view(), name='bw3backend_orga_location_update'),
)

urlpatterns += (
    # urls for orga_vehical
    path('bw3backend/orga_vehical/', views.orga_vehicalListView.as_view(), name='bw3backend_orga_vehical_list'),
    path('bw3backend/orga_vehical/create/', views.orga_vehicalCreateView.as_view(), name='bw3backend_orga_vehical_create'),
    path('bw3backend/orga_vehical/detail/<int:pk>/', views.orga_vehicalDetailView.as_view(), name='bw3backend_orga_vehical_detail'),
    path('bw3backend/orga_vehical/update/<int:pk>/', views.orga_vehicalUpdateView.as_view(), name='bw3backend_orga_vehical_update'),
)

urlpatterns += (
    # urls for plugin_config
    path('bw3backend/plugin_config/', views.plugin_configListView.as_view(), name='bw3backend_plugin_config_list'),
    path('bw3backend/plugin_config/create/', views.plugin_configCreateView.as_view(), name='bw3backend_plugin_config_create'),
    path('bw3backend/plugin_config/detail/<int:pk>/', views.plugin_configDetailView.as_view(), name='bw3backend_plugin_config_detail'),
    path('bw3backend/plugin_config/update/<int:pk>/', views.plugin_configUpdateView.as_view(), name='bw3backend_plugin_config_update'),
)

urlpatterns += (
    # urls for dataincoming
    path('bw3backend/dataincoming/', views.dataincomingListView.as_view(), name='bw3backend_dataincoming_list'),
    path('bw3backend/dataincoming/create/', views.dataincomingCreateView.as_view(), name='bw3backend_dataincoming_create'),
    path('bw3backend/dataincoming/detail/<int:pk>/', views.dataincomingDetailView.as_view(), name='bw3backend_dataincoming_detail'),
    path('bw3backend/dataincoming/update/<int:pk>/', views.dataincomingUpdateView.as_view(), name='bw3backend_dataincoming_update'),
)

urlpatterns += (
    # urls for helper_datatype
    path('bw3backend/helper_datatype/', views.helper_datatypeListView.as_view(), name='bw3backend_helper_datatype_list'),
    path('bw3backend/helper_datatype/create/', views.helper_datatypeCreateView.as_view(), name='bw3backend_helper_datatype_create'),
    path('bw3backend/helper_datatype/detail/<int:pk>/', views.helper_datatypeDetailView.as_view(), name='bw3backend_helper_datatype_detail'),
    path('bw3backend/helper_datatype/update/<int:pk>/', views.helper_datatypeUpdateView.as_view(), name='bw3backend_helper_datatype_update'),
)

urlpatterns += (
    # urls for plugininstance_config
    path('bw3backend/plugininstance_config/', views.plugininstance_configListView.as_view(), name='bw3backend_plugininstance_config_list'),
    path('bw3backend/plugininstance_config/create/', views.plugininstance_configCreateView.as_view(), name='bw3backend_plugininstance_config_create'),
    path('bw3backend/plugininstance_config/detail/<int:pk>/', views.plugininstance_configDetailView.as_view(), name='bw3backend_plugininstance_config_detail'),
    path('bw3backend/plugininstance_config/update/<int:pk>/', views.plugininstance_configUpdateView.as_view(), name='bw3backend_plugininstance_config_update'),
)

urlpatterns += (
    # urls for globalconfig
    path('bw3backend/globalconfig/', views.globalconfigListView.as_view(), name='bw3backend_globalconfig_list'),
    path('bw3backend/globalconfig/create/', views.globalconfigCreateView.as_view(), name='bw3backend_globalconfig_create'),
    path('bw3backend/globalconfig/detail/<int:pk>/', views.globalconfigDetailView.as_view(), name='bw3backend_globalconfig_detail'),
    path('bw3backend/globalconfig/update/<int:pk>/', views.globalconfigUpdateView.as_view(), name='bw3backend_globalconfig_update'),
)

