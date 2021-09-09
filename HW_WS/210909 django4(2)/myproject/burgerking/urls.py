from django.urls import path
from . import views

app_name = 'burgerking'
urlpatterns = [
    path('', views.index, name='index'),
    path('menu', views.menu, name='menu'),
    path('create', views.create, name='create'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/update', views.update, name='update'),
    path('<int:pk>/delete', views.delete, name='delete'),
]
