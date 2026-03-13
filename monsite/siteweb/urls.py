from django.urls import path
from . import views

urlpatterns = [
    path('', views.accuiel, name="accuiel"),
    path('contact/', views.contact, name="contact"),
    path('about/', views.about, name="about"),
    path('actualite/', views.actualite, name="actualite"),
    path('academique/', views.academique, name="academique"),
    path('campus/', views.campus, name="campus"),
]