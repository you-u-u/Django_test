from django.urls import path
from . import views

urlpatterns = [
    path('sora/', views.customer_list, name = 'customer_list' )
]
