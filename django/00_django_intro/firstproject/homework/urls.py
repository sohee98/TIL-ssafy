from django.urls import path
from . import views

app_name = 'homework'
urlpatterns = [
    path('hw/', views.hw, name='hw'),
]