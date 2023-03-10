from django.urls import path
#from . import views
#from django.conf.urls import url #pas sur que la ligne soit utile
from sellers.views import *
urlpatterns = [
   path('index2', index2, name='index2'),
   path('http-response/', http_response), 
   path('http-response-form', http_response_form, name="httpresponse"),
   path('home/', home_form, name="home"),
   path('person',personDetails),
   path('getAllPersons',getAllPersons),
   path('city',cityDetails),
   path('getAllCities',getAllCities),
   path('connectPaC',connectPaC),
   path('connectPaP',connectPaP)
]