from django.urls import path
from dj_appli import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home', views.home, name='home'),
    path('educative/', views.educative, name='educative'),
]
