
from django.http import *
from django.template import RequestContext,loader

from django.shortcuts import render
def index(request):
    # temp = loader.get_template('index.html')
    # return HttpResponse(temp.render())
    return render(request,'index.html')