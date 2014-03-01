from django.shortcuts import render
from django.shortcuts import render_to_response
from django.conf import settings
import json

import requests

def results(request):
  api_url = settings.API_URL
  results = requests.get(api_url)
  resp = json.loads(results.content)
  portfolios = resp["objects"]
  red_c = []
  for portfolio in portfolios:
    if portfolio['color'] == 'R':
      red_c.append(portfolio)
  return render_to_response('clientui/results.html', locals())
