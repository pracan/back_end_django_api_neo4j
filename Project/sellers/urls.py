from django.urls import path
from . import views

urlpatterns = [
   path('', views.index2, name='index2'),
   path('http-response/', views.http_response), 
   path('http-response-form', views.http_response_form, name="httpresponse"),
   path('home/', views.home_form, name="home")
]