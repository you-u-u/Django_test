from django.urls import path
from .views import CustomerList, DetailCustomer

app_name = 'sora'

urlpatterns = [
  path('customers', CustomerList.as_view(), name = 'index'),
  path('customer/<int:pk>/detail/', DetailCustomer.as_view(), name = 'detail_customer'),
]
