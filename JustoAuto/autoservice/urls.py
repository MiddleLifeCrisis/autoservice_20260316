from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('kainorastis/', views.kainorastis, name='kainorastis'),
    path('about/', views.about, name='about'),
    path('cars/', views.cars, name='cars'),
    path('car/<int:car_id>/', views.car, name='car'),
    path('orders/', views.OrderListView.as_view(), name='orders'),
    path('orders/<int:pk>/', views.OrderDetailView.as_view(), name='order-detail'),
    path('search/', views.search, name='search'),
    path('myorders/', views.MyOrderInstanceListView.as_view(), name='myorders'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path("profile/", views.UserUpdateView.as_view(), name="profile"),
    path("profile/", views.profile, name="profile"),
    path('myorders/', views.MyOrderInstanceListView.as_view(), name='my-orders'), # <--- Svarbu šis 'name'
    path('orders/<int:pk>/update/', views.OrderUpdateView.as_view(), name='order-update'),
    path('orders/<int:pk>/delete/', views.OrderDeleteView.as_view(), name='order-delete'),
    path('orders/new/', views.create_order, name='order-create'),
]

