from django.db import models

# Create your models here.

class Color(models.Model):
  CHOICES = ( (u'B', 'Blue'), (u'G', 'Green'), (u'R', 'Red'))
  color   = models.CharField(max_length=1, choices=CHOICES, default='G')
