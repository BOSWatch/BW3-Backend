from django.urls import reverse
from django_extensions.db.fields import AutoSlugField
from django.db.models import *
from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import get_user_model
from django.contrib.auth import models as auth_models
from django.db import models as models
from django_extensions.db import fields as extension_fields
import django 



class helper_datatype(models.Model):

    # Fields
    name = models.CharField(max_length=30)


    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('bw3backend_helper_datatype_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('bw3backend_helper_datatype_update', args=(self.pk,))

    def __str__(self):
	    return u'%s' % self.name
		
				
		
class data(models.Model):

    # Fields
    direction = models.BooleanField()
    callid = models.CharField(max_length=100)

    # Relationship Fields
    type = models.ForeignKey(helper_datatype,on_delete=models.CASCADE)

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
		
		

class client(models.Model):

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
		
		
class client_config(models.Model):

    # Fields
    setting = models.CharField(max_length=100)
    value = CharField(max_length=255)
    front_name = models.CharField(max_length=30, blank=True)
    front_description = models.TextField(max_length=500, blank=True)

	
    # Relationship Fields
    client = models.ForeignKey(client,on_delete=models.CASCADE)

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
	
class plugin(models.Model):

    # Fields
    name = CharField(max_length=255)
    version = DecimalField(max_digits=3, decimal_places=2)
    builddate = DateField()
    creator = CharField(max_length=30)
    possibledatatypes = models.ManyToManyField(helper_datatype,blank=True,null=True)
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
	
class plugininstance(models.Model):

    # Fields
    front_name = models.CharField(max_length=50, blank=True)
    name = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    active = models.BooleanField(default=1)


    # Relationship Fields
    plugin = models.ForeignKey(plugin,on_delete=models.CASCADE)
    createdby = models.ForeignKey(django.contrib.auth.models.User,on_delete=models.CASCADE)

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
	

class orga_location(models.Model):

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
		
class orga_vehical(models.Model):

    # Fields
    name = CharField(max_length=255)
    optaname = CharField(max_length=30)
    numberplate = TextField(max_length=30)

	
	# hier fehlen noch tags ... 

    # Relationship Fields
    fmskennung = models.ForeignKey(data, on_delete=models.CASCADE)

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
		
class orga_units(models.Model):

    # Fields
    name = models.CharField(max_length=150)
    description = models.TextField(max_length=255)
    optaname = models.TextField(max_length=75)
    inheritalarm = models.BooleanField(default=True)

    # Relationship Fields
    location = models.ForeignKey(orga_location,blank=True,null=True,on_delete=models.CASCADE)
    vehicals = models.ManyToManyField(orga_vehical,blank=True,null=True) 
    parent = models.ForeignKey('self',blank=True,null=True,on_delete=models.CASCADE)

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
class plugin_config(models.Model):

    # Fields
    setting = models.CharField(max_length=100)
    value = models.CharField(max_length=255)
    front_name = models.CharField(max_length=30)
    front_description = models.TextField(max_length=500, blank=True)

    # Relationship Fields
    plugin = models.ForeignKey(plugin,on_delete=models.CASCADE)

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
		
class dataincoming(models.Model):

    # Fields
    created = models.DateTimeField(auto_now_add=True)
    cliententrytime = models.DateTimeField()
    workload = models.CharField(max_length=255)
    direction = models.BooleanField()
    

    # Relationship Fields
    callid = models.ForeignKey(data,on_delete=models.CASCADE)
    client = models.ForeignKey(client,on_delete=models.CASCADE)

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

class plugininstance_config(models.Model):

    # Fields
    setting = models.CharField(max_length=100)
    value = models.CharField(max_length=255)

    # Relationship Fields
    plugininstance = models.ForeignKey(plugininstance,on_delete=models.CASCADE)

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
		
class globalconfig(models.Model):

    # Fields
    setting = models.CharField(max_length=100)
    value = models.CharField(max_length=255)


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
