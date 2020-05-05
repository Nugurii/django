from django.urls import path, include
from django.contrib import admin
from myapp import views
 
app_name = 'user19'
 
urlpatterns = [
    path('admin', admin.site.urls),
    path('myapp/', views.login),
    path('index/', views.index),
    path('register/', views.register),
    path('logout/', views.logout),
]