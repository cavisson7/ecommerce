from django.urls import path
from .import views
from rest_framework.urlpatterns import format_suffix_patterns
from webapp import views
from ecom import views
from django.contrib import admin
urlpatterns = [
    path("", views.home,name="home"),
    path("logout",views.logout, name="logout"),
    path("contact",views.contact,name="contact")
    
]