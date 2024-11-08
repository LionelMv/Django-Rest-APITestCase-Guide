from django.urls import path
from .views import (
    CustomerListCreateView,
    CustomerRetrieveUpdateDestroyView,
    OrderListCreateView,
    OrderRetrieveUpdateDestroyView
)

urlpatterns = [
    # Customer Endpoints
    path('customers/', CustomerListCreateView.as_view(),
         name='customer-list'),
    path('customers/<int:pk>/', CustomerRetrieveUpdateDestroyView.as_view(),
         name='customer-detail'),

    # Order Endpoints
    path('orders/', OrderListCreateView.as_view(),
         name='order-list'),
    path('orders/<int:pk>/', OrderRetrieveUpdateDestroyView.as_view(),
         name='order-detail'),
]
