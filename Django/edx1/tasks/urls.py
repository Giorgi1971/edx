from django.urls import path
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.add, name='add'),
]

