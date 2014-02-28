from django.shortcuts import render
from django.shortcuts import render_to_response

def results(request):
  print 'I am here'
  return render_to_response('clientui/results.html', locals())
