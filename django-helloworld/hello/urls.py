from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello_world, name='hello_world'),
    path('hello/', views.hello_world, name='hello_world_link'),
]
