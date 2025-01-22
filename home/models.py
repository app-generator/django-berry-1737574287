# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__
    sellertype = models.TextField(max_length=255, null=True, blank=True)

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Bikes(models.Model):

    #__Bikes_FIELDS__
    id = models.IntegerField(null=True, blank=True)
    year = models.TextField(max_length=255, null=True, blank=True)
    make = models.TextField(max_length=255, null=True, blank=True)
    model = models.TextField(max_length=255, null=True, blank=True)
    mileage = models.TextField(max_length=255, null=True, blank=True)
    color = models.TextField(max_length=255, null=True, blank=True)
    tmu = models.BooleanField()
    cleantitle = models.BooleanField()
    payoff = models.TextField(max_length=255, null=True, blank=True)
    overall condition = models.TextField(max_length=255, null=True, blank=True)

    #__Bikes_FIELDS__END

    class Meta:
        verbose_name        = _("Bikes")
        verbose_name_plural = _("Bikes")


class Communications(models.Model):

    #__Communications_FIELDS__
    type = models.TextField(max_length=255, null=True, blank=True)
    body = models.TextField(max_length=255, null=True, blank=True)

    #__Communications_FIELDS__END

    class Meta:
        verbose_name        = _("Communications")
        verbose_name_plural = _("Communications")



#__MODELS__END
