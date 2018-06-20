# -*- coding: utf-8 -*-
from django.shortcuts import render
import datetime
from django.utils.timezone import now

def home(request):
    t = datetime.date.today()
    return render(request, 'ekozmp/index.html', {'today': t, 'now': now()})

def home_files(request, filename):
    return render(request, filename, {}, content_type='text/plain')
