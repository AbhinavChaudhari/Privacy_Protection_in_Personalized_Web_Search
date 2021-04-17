from django.urls import path
from . import views

urlpatterns = [
    path('homepage', views.index, name='homepage'),
    path('search', views.search, name='search'),
    path('histroy', views.histroy, name='histroy'),
]