# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from .models import Target

def index(request):
    return render(request, 'vision/index.html')

def target_view(request, target_id):
    return HttpResponse("Looking at target %s." % target_id)

def targets(request):
    targets_list = Target.objects.order_by('-id')
    context = {'targets_list': targets_list}
    return render(request, 'vision/targets.html', context)
# Create your views here.
