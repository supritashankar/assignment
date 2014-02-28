from django.conf.urls import patterns, include, url
from portfolio.api import ColorResource
from django.contrib import admin
admin.autodiscover()

color_resource = ColorResource()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^clientui/',include('clientui.urls')),
    url(r'^api/', include(color_resource.urls)),
)
