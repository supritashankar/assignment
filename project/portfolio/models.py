from django.db import models

# Create your models here.

class Portfolio(models.Model):
  CHOICES = ( (u'B', 'Blue'), (u'G', 'Green'), (u'R', 'Red'))
  color   = models.CharField(max_length=1, choices=CHOICES, default='G')
  description = models.CharField(max_length = 100)

  def __unicode__(self):
    return "You created an object of color {0}".format(self.color)
