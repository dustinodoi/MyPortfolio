from django import views
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name = "index"),
    path("About/", views.About, name = "About"),
    path("contact/", views.contact, name = "contact"),
    path("Portfolio/", views.Portfolio, name = "Portfolio"),
    path("Resume/", views.Resume, name = "Resume")
    

]
