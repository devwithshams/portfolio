from django.urls import path
from . import views


urlpatterns = [
    path('', views.homePage, name='home'),
    path('cv/', views.resume, name='cv'),
    path('contact/', views.contact, name='contact'),
    path('lists/', views.ListView, name='lists'),
]
