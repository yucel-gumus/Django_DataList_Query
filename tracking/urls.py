from django.urls import path
from . import views

urlpatterns = [
    path('', views.last_locations, name='index'),
]
