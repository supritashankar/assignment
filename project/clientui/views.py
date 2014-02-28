from django.shortcuts import render
from django.shortcuts import render_to_response
import json

import requests

def results(request):
  api_url = "http://127.0.0.1:8000/api/color/?format=json"
  results = requests.get(api_url)
  resp = json.loads(results.content)
  colors = resp["objects"]
  return render_to_response('clientui/results.html', locals())
