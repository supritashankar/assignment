from django.shortcuts import render
from django.shortcuts import render_to_response
from django.conf import settings
import json

import requests

def results(request):
  api_url = settings.API_URL
  results = requests.get(api_url)
  resp = json.loads(results.content)
  colors = resp["objects"]

  """ Filter according to results
      red_c = colors.filter('color' == 'R')
      similarly for blue and green
  """

  return render_to_response('clientui/results.html', locals())
