# myapp/api.py
from tastypie.resources import ModelResource
from portfolio.models import Portfolio
from tastypie.authorization import Authorization

class PortfolioResource(ModelResource):
    class Meta:
        queryset = Portfolio.objects.all()
        resource_name = 'portfolio'
	authorization = Authorization()
	allowed_methods = ['get', 'put']
