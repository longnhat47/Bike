
from django.contrib import admin
from django.urls import path, include

from core import views
from orders.views import RentBikeView, RentListView, OrderListView, OrderDetailView, DeleteOrder

urlpatterns = [
    path('rent-bike/<uuid:pk>/', RentBikeView.as_view(), name='rent-bike'),
    path('rent-list/', RentListView.as_view(), name='rent-list'),
    path('order-admin', OrderListView.as_view(), name='order-admin'),
    path('order-detail-admin/<uuid:id>', OrderDetailView.as_view(), name='order-detail-admin'),
    path('delete-order/<uuid:pk>', DeleteOrder.as_view(), name='delete-order')
]
