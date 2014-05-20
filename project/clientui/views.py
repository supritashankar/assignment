from django.shortcuts import render
from django.shortcuts import render_to_response
from django.conf import settings
from django.core.context_processors import csrf
from django.template import RequestContext
from django.http import HttpResponse

import json
import requests

from clientui.forms import PortfolioUpdateForm

def results(request):
  form = PortfolioUpdateForm()
  if request.method == 'POST':
    form = PortfolioUpdateForm(request.POST)
    if form.is_valid():
      color_choice = '"' + form.cleaned_data['color_choices'] + '"'
      data = '{"color":' + str(color_choice) + '}'
      url = settings.API_UPDATE_URL + form.cleaned_data['object_id'] +"/"
      headers = {"Content-Type": "application/json"}
      response = requests.put( url,
                	       data=data,                         
                	       headers = headers,
                              )
      if response.status_code == 204:
        message = {'status' : 'ok', 'message': 'success'}
        return HttpResponse(json.dumps(message), mimetype = 'application/json')
      else:
 	message = {'status' : 'oops', 'message': 'error!!'}
        return HttpResponse(json.dumps(message), mimetype = 'application/json')

  api_url = settings.API_URL
  results = requests.get(api_url)
  resp = json.loads(results.content)
  portfolios = resp["objects"]

  red_c = []
  blue_c = []
  green_c =  []
  """ group by client side """
  for portfolio in portfolios:
    if portfolio['color'] == 'R':
      red_c.append(portfolio)
    elif portfolio['color'] == 'B':
      blue_c.append(portfolio)
    else:
      green_c.append(portfolio)
  return render_to_response('clientui/results.html', locals(), RequestContext(request))


def colors(request):
  return render_to_response('clientui/colors.html')

def retrieve_colors(request, color):
  if color == 'B':
   response = requests.get("http://127.0.0.1:8000/api/portfolio/?color=B")
   color = 'Blue'
   resp = json.loads(response.content)
   objs = resp["objects"]
  return render_to_response('clientui/color-results.html', locals(), RequestContext(request)) 
