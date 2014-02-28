from django.conf.urls import patterns, include, url
from portfolio.api import PortfolioResource
from django.contrib import admin
admin.autodiscover()

portfolio_resource = PortfolioResource()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^clientui/',include('clientui.urls')),
    url(r'^api/', include(portfolio_resource.urls)),
)
