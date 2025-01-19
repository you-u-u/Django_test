from django.contrib import admin

# Register your models here.
from .models import Customer,PurchaseHistory

admin.site.register(Customer)
admin.site.register(PurchaseHistory)
