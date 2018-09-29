import django
from django.contrib.auth import get_user_model
from django.db import models as models
from django.db.models import *
from django.urls import reverse


# Hier werden alle Datentypen definiert (wie z.B. FMS,POCSAG,ZVEI,ServerMsg,etc.)
class Helper_Datatype(models.Model):
    # Fields
    name = models.CharField(max_length=30)

    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def __str__(self):
        return u'%s' % self.name


# Hier werden alle HTML Input-Methoden definiert

class Helper_Inputtype(models.Model):
    # Fields
    name = models.CharField(max_length=30)
    value = models.CharField(max_length=30)

    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def __str__(self):
        return u'%s' % self.name

# Hier wird jede bekannte Adresse angegeben, für AutoFillIn später Mal...
class Data(models.Model):
    # Fields
    direction = models.BooleanField()
    callid = models.CharField(max_length=100)

    # Relationship Fields
    type = models.ForeignKey(Helper_Datatype, on_delete=models.CASCADE)

    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('bw3backend_dataincoming_detail', args=(self.pk,))

    def get_update_url(self):
        return reverse('bw3backend_dataincoming_update', args=(self.pk,))

    def __str__(self):
        return u'%s' % self.callid

# Clienten die Daten zum Server senden dürfen. bzw. ihre Konfiguration bekommen.
class Client(models.Model):
    # Fields
    name = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    password = models.CharField(max_length=32)
    lastseen = models.DateTimeField(auto_now_add=True, editable=True)

    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('bw3backend_client_detail', args=(self.pk,))

    def get_update_url(self):
        return reverse('bw3backend_client_update', args=(self.pk,))

    def __str__(self):
        return u'%s' % self.name

# Configurationstabelle für die Clients
class Client_Config(models.Model):
    # Fields
    order = models.IntegerField(default=100, unique=True)                       # Hiernach wird im WebFront geordnet, bedeutet Einstellungen die weit oben stehen sollen bekommen eine kleine Zahl
    setting = models.CharField(max_length=100, unique=True)                     # Interner Name des Settings
    value = models.CharField(max_length=255, blank=True)                        # Wert
    front_name = models.CharField(max_length=50, blank=True)                    # Name im Frontend
    front_description = models.TextField(max_length=500, blank=True)            # Beschreibung im Frontend
    pattern = models.CharField(max_length=100, blank=True)                      # HTML5 Pattern um Eingabe direkt zu filtern

    inputtype = models.ForeignKey(Helper_Inputtype, on_delete=models.CASCADE)   # Art der Darstellung im Frontend
    # Relationship Fields
    client = models.ForeignKey(Client, on_delete=models.CASCADE)                # Verweis auf den Client

    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('bw3backend_client_config_detail', args=(self.pk,))

    def get_update_url(self):
        return reverse('bw3backend_client_config_update', args=(self.pk,))

    def __str__(self):
        return u'%s' % self.setting


class Plugin(models.Model):
    # Fields
    name = CharField(max_length=255)
    version = DecimalField(max_digits=3, decimal_places=2)
    builddate = DateField()
    creator = CharField(max_length=30)
    possibledatatypes = models.ManyToManyField(Helper_Datatype, blank=True)
    needsinternet = models.BooleanField(default=0)
    front_name = models.CharField(max_length=50, blank=True)
    front_description = models.TextField(max_length=500, blank=True)

    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('bw3backend_plugin_detail', args=(self.pk,))

    def get_update_url(self):
        return reverse('bw3backend_plugin_update', args=(self.pk,))

    def __str__(self):
        return u'%s' % self.name


class PluginInstance(models.Model):
    # Fields
    front_name = models.CharField(max_length=50, blank=True)
    name = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    active = models.BooleanField(default=1)

    # Relationship Fields
    plugin = models.ForeignKey(Plugin, on_delete=models.CASCADE)
    createdby = models.ForeignKey(django.contrib.auth.models.User, on_delete=models.CASCADE)

    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('bw3backend_plugininstance_detail', args=(self.pk,))

    def get_update_url(self):
        return reverse('bw3backend_plugininstance_update', args=(self.pk,))

    def __str__(self):
        return u'%s' % self.name


class Orga_Location(models.Model):
    # Fields
    name = CharField(max_length=255)
    addr_street = CharField(max_length=30)
    addr_nr = CharField(max_length=5)
    addr_plz = CharField(max_length=10)
    addr_city = CharField(max_length=30)
    telephone = CharField(max_length=30)

    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('bw3backend_orga_location_detail', args=(self.pk,))

    def get_update_url(self):
        return reverse('bw3backend_orga_location_update', args=(self.pk,))

    def __str__(self):
        return u'%s' % self.name


class Orga_Vehical(models.Model):
    # Fields
    name = CharField(max_length=255)
    optaname = CharField(max_length=30)
    numberplate = TextField(max_length=30)

    # hier fehlen noch tags ...

    # Relationship Fields
    fmskennung = models.ForeignKey(Data, on_delete=models.CASCADE)

    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('bw3backend_orga_vehical_detail', args=(self.pk,))

    def get_update_url(self):
        return reverse('bw3backend_orga_vehical_update', args=(self.pk,))

    def __str__(self):
        return u'%s' % self.name


class Orga_Units(models.Model):
    # Fields
    name = models.CharField(max_length=150)
    description = models.TextField(max_length=255)
    optaname = models.TextField(max_length=75)
    inheritalarm = models.BooleanField(default=True)

    # Relationship Fields
    location = models.ForeignKey(Orga_Location, blank=True, on_delete=models.CASCADE)
    vehicals = models.ManyToManyField(Orga_Vehical, blank=True)
    parent = models.ForeignKey('self', blank=True, null=True, on_delete=models.CASCADE)

    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('bw3backend_orga_units_detail', args=(self.pk,))

    def get_update_url(self):
        return reverse('bw3backend_orga_units_update', args=(self.pk,))

    def __str__(self):
        return u'%s' % self.name


class Plugin_Config(models.Model):
    # Fields
    order = models.IntegerField(default=100, unique=True)
    setting = models.CharField(max_length=100, unique=True)
    value = models.CharField(max_length=255, blank=True)
    front_name = models.CharField(max_length=50, blank=True)
    front_description = models.TextField(max_length=500, blank=True)
    pattern = models.CharField(max_length=100, blank=True)

    inputtype = models.ForeignKey(Helper_Inputtype, on_delete=models.CASCADE)
    # Relationship Fields
    plugin = models.ForeignKey(Plugin, on_delete=models.CASCADE)

    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('bw3backend_plugin_config_detail', args=(self.pk,))

    def get_update_url(self):
        return reverse('bw3backend_plugin_config_update', args=(self.pk,))

    def __str__(self):
        return u'%s' % self.setting


class DataIncoming(models.Model):
    # Fields
    created = models.DateTimeField(auto_now_add=True)
    cliententrytime = models.DateTimeField()
    workload = models.CharField(max_length=255)
    direction = models.BooleanField()

    # Relationship Fields
    callid = models.ForeignKey(Data, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)

    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('bw3backend_dataincoming_detail', args=(self.pk,))

    def get_update_url(self):
        return reverse('bw3backend_dataincoming_update', args=(self.pk,))

    def __str__(self):
        return u'%s' % self.callid


class PluginInstance_Config_Template(models.Model):
    # Fields
    order = models.IntegerField(default=100, unique=True)
    setting = models.CharField(max_length=100, unique=True)
    default_value = models.CharField(max_length=255, blank=True)
    front_name = models.CharField(max_length=50, blank=True)
    front_description = models.TextField(max_length=500, blank=True)
    pattern = models.CharField(max_length=100, blank=True)

    inputtype = models.ForeignKey(Helper_Inputtype, on_delete=models.CASCADE)
    # Relationship Fields
    plugin = models.ForeignKey(Plugin, on_delete=models.CASCADE)

    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('bw3backend_plugininstance_config_detail', args=(self.pk,))

    def get_update_url(self):
        return reverse('bw3backend_plugininstance_config_update', args=(self.pk,))

    def __str__(self):
        return u'%s' % self.setting


class PluginInstance_Config(models.Model):
    # Fields
    value = models.CharField(max_length=255)

    # Relationship Fields
    plugininstance = models.ForeignKey(PluginInstance, on_delete=models.CASCADE)
    template = models.ForeignKey(PluginInstance_Config_Template, on_delete=models.CASCADE)



    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('bw3backend_plugininstance_config_detail', args=(self.pk,))

    def get_update_url(self):
        return reverse('bw3backend_plugininstance_config_update', args=(self.pk,))

    def __str__(self):
        return u'%s' % self.template


class GlobalConfig_Section(models.Model):
    order = models.IntegerField(default=100, unique=True)
    front_name = models.CharField(max_length=50)
    front_description = models.TextField(max_length=500, blank=True)

    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('bw3backend_globalconfig_detail', args=(self.pk,))

    def get_update_url(self):
        return reverse('bw3backend_globalconfig_update', args=(self.pk,))

    def __str__(self):
        return u'%s' % self.front_name


class GlobalConfig(models.Model):
    # Fields
    order = models.IntegerField(default=100, unique=True)
    setting = models.CharField(max_length=100, unique=True)
    value = models.CharField(max_length=255, blank=True)
    front_name = models.CharField(max_length=50, blank=True)
    front_description = models.TextField(max_length=500, blank=True)
    pattern = models.CharField(max_length=100, blank=True)

    inputtype = models.ForeignKey(Helper_Inputtype, on_delete=models.CASCADE)
    section = models.ForeignKey(GlobalConfig_Section, on_delete=models.CASCADE)

    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('bw3backend_globalconfig_detail', args=(self.pk,))

    def get_update_url(self):
        return reverse('bw3backend_globalconfig_update', args=(self.pk,))

    def __str__(self):
        return u'%s' % self.setting
