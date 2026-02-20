from django.contrib import admin
from django.urls import path
from hello import views

urlpatterns = [
    path('admin/', admin.site.name),
    path('', views.hello_world, name='index'),    # This handles the main page
    path('hello/', views.hello_world, name='hello_world'), # Add this line for the button!
]
