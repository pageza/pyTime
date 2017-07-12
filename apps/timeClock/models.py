# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=38)
    last_name = models.CharField(max_length=38)
    division = models.CharField(max_length=20)
    employee_number = models.IntegerField()
    age = models.IntegerField()
    payrate = models.IntegerField()
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    admin = models.BooleanField(default=False)
class Job(models.Model):
    def __unicode__(self):
        return u'{0}'.format(self.title)
    title = models.CharField(max_length=30)
class Location(models.Model):
    def __unicode__(self):
        return u'{0}'.format(self.street)
    street = models.CharField(max_length=25)
    city = models.CharField(max_length=25)
    state = models.CharField(max_length=2)
class Clock_in(models.Model):
    user = models.ForeignKey(User, related_name="clock_ins")
    location = models.ForeignKey(Location, related_name="location_in")
    job = models.ForeignKey(Job, related_name="job_in")
    time = models.DateTimeField(auto_now_add=True)
    notes = models.CharField(max_length=255)
class Clock_out(models.Model):
    user = models.ForeignKey(User, related_name="clock_outs")
    location = models.ForeignKey(Location, related_name="location_out")
    job = models.ForeignKey(Job, related_name="job_out")
    time = models.DateTimeField(auto_now_add=True)
    notes = models.CharField(max_length=255)
    lunch = models.BooleanField(default=False)
class Company_notices(models.Model):
    message = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)