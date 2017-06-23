# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from .models import Target, CamUrl

def index(request):
    return render(request, 'vision/index.html')

def target_view(request, target_id):
    target = Target.objects.get(id=target_id)
    context = {'target': target}
    return render(request, 'vision/single_target.html', context)

def targets(request):
    targets_list = Target.objects.order_by('-id')
    context = {'targets_list': targets_list}
    return render(request, 'vision/targets.html', context)

def cam_stream_view(request):
    camurl = CamUrl.objects.get(id=1)
    context = {'camurl': camurl.camurl}
    return render(request, 'vision/stream.html', context)

def improcess(request):
    return render(request, 'vision/improcess.html')
