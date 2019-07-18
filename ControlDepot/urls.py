from django.urls import path
from . import views

urlpatterns = [
    path('', views.ControlDepot, name='ControlDepot'),
]
