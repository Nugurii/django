from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.home),
    path('user/signin/', views.signin),
    path('user/signup/', views.signup),
    path('user/logout/', views.logout),
]