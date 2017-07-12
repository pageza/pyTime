from django import forms
from django.db import models
from .models import *
from django.forms import ModelChoiceField



class LogInForm(forms.Form):
    employee_number = forms.IntegerField()
    password = forms.CharField(max_length=255, widget=forms.PasswordInput)

class ClockInForm(forms.Form):
    locations = Location.objects.all()
    location = forms.ModelChoiceField(queryset=locations)
    jobs = Job.objects.all()
    job = forms.ModelChoiceField(queryset=jobs, to_field_name="title")
    note = forms.CharField(max_length=1000, widget=forms.Textarea)