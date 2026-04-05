from django.contrib import admin
from django.urls import path
from hello import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index_view, name='index'),                     # http://35.90.198.162/
    path('hello/', views.hello_world, name='hello'),              # http://35.90.198.162/hello/
    path('hello/register/', views.register_view, name='register'),# http://35.90.198.162/hello/register/
    path('hello/login/', views.login_view, name='login'),         # http://35.90.198.162/hello/login/
    path('hello/logout/', views.logout_view, name='logout'),      # http://35.90.198.162/hello/logout/
]