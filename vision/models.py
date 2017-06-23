# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class GpsPosition(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()

class CamUrl(models.Model):
    camurl = models.TextField(default='http://169.254.171.248/mjpg/video.mjpg', blank=True)
    
class Target(models.Model):
    target_type = models.TextField(default='standard', blank=True)
    location = models.ForeignKey(GpsPosition, null=True, blank=True)
    orientation = models.TextField(default='', blank=True)
    shape = models.TextField(default='', blank=True)
    background_color = models.TextField(default='', blank=True)
    alphanumeric = models.TextField(default='', blank=True)
    alphanumeric_color = models.TextField(default='', blank=True)
    description = models.TextField(default='', blank=True)
    thumbnail = models.ImageField(upload_to='targets', blank=True)
    creation_time = models.DateTimeField(auto_now_add=True)
    last_modifified_time = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        """Descriptive text for use in displays"""
        d = self.json()
        return unicode('{name}({fields})'.format(
            name=self.__class__.__name__,
            fields=', '.join('%s=%s' % (k, v) for k, v in d.iteritems())))

    def json(self):
        """Target as dict, for JSON."""
        target_type = None
        if self.target_type is not None:
            target_type = self.target_type

        latitude = None
        longitude = None
        if self.location is not None:
            latitude = self.location.latitude
            longitude = self.location.longitude

        orientation = None
        if self.orientation is not None:
            orientation = self.orientation

        shape = None
        if self.shape is not None:
            shape = self.shape

        background_color = None
        if self.background_color is not None:
            background_color = self.background_color

        alphanumeric = None
        if self.alphanumeric != '':
            alphanumeric = self.alphanumeric

        alphanumeric_color = None
        if self.alphanumeric_color is not None:
            alphanumeric_color = self.alphanumeric_color

        description = None
        if self.description != '':
            description = self.description

        d = {
            'id': self.pk,
            'type': target_type,
            'latitude': latitude,
            'longitude': longitude,
            'orientation': orientation,
            'shape': shape,
            'background_color': background_color,
            'alphanumeric': alphanumeric,
            'alphanumeric_color': alphanumeric_color,
            'description': description,
        }

        return d
