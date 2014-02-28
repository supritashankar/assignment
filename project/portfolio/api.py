# myapp/api.py
from tastypie.resources import ModelResource
from portfolio.models import Color


class ColorResource(ModelResource):
    class Meta:
        queryset = Color.objects.all()
        resource_name = 'color'
