from django.urls import path
from . import views

urlpatterns = [
    path('', views.ControlDepot_list, name='ControlDepot_list'),
]
