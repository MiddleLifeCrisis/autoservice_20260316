from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('kainorastis/', views.kainorastis, name='kainorastis'),
    path('about/', views.about, name='about'),
]