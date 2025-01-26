from django import forms
from .models import Customer


class CustomerForm(forms.ModelForm):
  class Meta:
    model = Customer
    fields = [
      'last_name',
      'first_name',
      'last_name_kana',
      'first_name_kana',
      'address',
      'phone_number',
      'email',
    ]
    labels = {
      'first_name': '名',
      'last_name': '姓',
      'first_name_kana': '名（カナ）',
      'last_name_kana': '姓（カナ）',
      'address': '住所',
      'phone_number': '電話番号',
      'email': 'メールアドレス',
    }