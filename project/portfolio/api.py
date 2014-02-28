# myapp/api.py
from tastypie.resources import ModelResource
from portfolio.models import Color
from tastypie.authorization import Authorization

class ColorResource(ModelResource):
    class Meta:
        queryset = Color.objects.all()
        resource_name = 'color'
	authorization = Authorization()
	allowed_methods = ['get', 'put']
