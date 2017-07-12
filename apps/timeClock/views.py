# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from .forms import *

# Create your views here.
def index(request):
    form = LogInForm()
    context = {
        "LogInForm": form
    }
    return render(request, 'timeClock/index.html',context)

def dashboard(request):
    form1 = ClockInForm()
    context = {
        "ClockInForm": form1
    }
    return render(request, 'timeClock/dashboard.html', context)