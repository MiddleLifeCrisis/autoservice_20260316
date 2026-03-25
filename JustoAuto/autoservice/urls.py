from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('kainorastis/', views.kainorastis, name='kainorastis'),
    path('about/', views.about, name='about'),
    path('cars/', views.cars, name='cars'),
    path('car/<int:car_id>/', views.car, name='car'),
    path('orders/', views.OrderListView.as_view(), name='orders'),
    path('orders/<int:pk>/', views.OrderDetailView.as_view(), name='order'),
    path('search/', views.search, name='search'),
]

