from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template

def index2(request):
   return HttpResponse("Hello sellers")
# Create your views here.

def http_response(request):
    return HttpResponse('<h1>Hello HttpResponse</h1>') 

def http_response_form(request):
    #template = get_template('HttpResponse.html')
    if request.method == "POST":
        username = request.POST.get('username')
        if username:
            return HttpResponse(f'<h1>hello {username}</h1>')
        else:
            return HttpResponse('<h1>please, enter your username</h1>')

    return render(request, 'HttpResponse.html')

def home_form(request):
    return render(request, "base.html")