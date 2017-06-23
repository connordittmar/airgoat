from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'targets/$', views.targets, name='targets'),
    url(r'targets/(?P<target_id>[0-9]+)/$', views.target_view, name = 'target_view'),
    url(r'stream/$', views.cam_stream_view, name='cam_stream_view'),
    url(r'improcess/$', views.improcess, name='improcess')
]
