# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from .models import Target

def index(request):
    return render(request, 'vision/index.html')

def target_view(request, target_id):
    return HttpResponse("Looking at target %s." % target_id)

def targets(request):
    target_list = Target.objects.order_by('-id')
    output = "Targets Overview: " + ', '.join([t.target_type for t in target_list])
    return HttpResponse(output)
# Create your views here.
