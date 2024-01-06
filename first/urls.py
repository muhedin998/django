from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"), 
    path('page1', views.page, name="page1")   
]
