from django.conf.urls import patterns, url
from django.views.generic import TemplateView

urlpatterns = patterns('clientui.views',
    url(r'^results/','results'),
    url(r'^colors/', 'colors'),
    url(r'^retrieve_colors/(?P<color>B|R|G)/$','retrieve_colors'))
