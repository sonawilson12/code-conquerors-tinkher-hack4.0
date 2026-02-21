from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('home/', views.home, name='home'),
    path('api/roadmap/', views.get_roadmap, name='get_roadmap'),
     path('home/', views.home, name='home'),
]



