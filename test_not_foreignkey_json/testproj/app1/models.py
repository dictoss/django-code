from django.db import models
from django.contrib import admin


class Thing(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return '%s - %s' % (self.id, self.name)
    
admin.site.register(Thing)


class ThingAttr(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    parent = models.ForeignKey(Thing, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return '%s - %s' % (self.id, self.name)

admin.site.register(ThingAttr)


class ThingAttr2(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    parent = models.IntegerField(null=True)

    def __str__(self):
        return '%s - %s' % (self.id, self.name)

admin.site.register(ThingAttr2)
