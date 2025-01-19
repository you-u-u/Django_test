# from django.shortcuts import render
# from django.http import JsonResponse
# from .models import Customer, PurchaseHistory
# from django.db.models import Q

# def customer_list(request):
#   Customers = Customer.objects.all
#   data = [
#     {
#       'id' = customer.id,
#       'full_name' = customer.full_name,
#       'full_name_kana' = customer.full_name_kana,
#       'purhase_history' = [
#         {
#           'pc_model' = history.pc_model,
#           'purchase_date' : history.purchase_date
#         } for history in customer.purshase_history.all()
#       ]
#     } for customer in customers
#   ]
#   return JsonResponse(data, safe=False)