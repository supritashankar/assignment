from django.shortcuts import render
from django.shortcuts import render_to_response
from django.conf import settings
from django.core.context_processors import csrf
from django.template import RequestContext

import json
import requests

from clientui.forms import PortfolioUpdateForm

def results(request):
  form = PortfolioUpdateForm()
  if request.method == 'POST':
    form = PortfolioUpdateForm(request.POST)
    if form.is_valid():
      color_choice = form.cleaned_data['color_choices']
      data = '{"color":' + str(color_choice) + '}'
      url = "http://127.0.0.1:8000/api/portfolio/" + form.cleaned_data['object_id'] + "/\?format\=json"
      response = requests.put( url,
                	       data=data,                         
                	       headers={'content-type':'application/json'},
                              )
      if response.status == 204:
        message = {'status' : 'ok', 'message': 'success'}
        return HttpResponse(simplejson.dumps(message), mimetype = 'application/json')
      else:
 	message = {'status' : 'oops', 'message': 'error!!'}
        return HttpResponse(json.dumps(message), mimetype = 'application/json')

  api_url = settings.API_URL
  results = requests.get(api_url)
  resp = json.loads(results.content)
  portfolios = resp["objects"]
  red_c = []
  for portfolio in portfolios:
    if portfolio['color'] == 'R':
      red_c.append(portfolio)
  return render_to_response('clientui/results.html', locals(), RequestContext(request))

