from django.db import models

# Create your models here.
class Customer(models.Model):
  first_name = models.CharField(max_length=100)
  last_name = models.CharField(max_length=100)
  first_name_kana = models.CharField(max_length=100, blank=True)
  last_name_kana = models.CharField(max_length=100, blank=True)
  address = models.CharField(max_length=255)
  phone_number = models.CharField(max_length=15)
  email = models.EmailField(unique=True)

  @property
  def full_name(self):
    return f'{self.last_name} {self.first_name}'
  
  @property
  def full_name_kana(self):
    return f'{self.last_name_kana} {self.first_name_kana}'
  
  def __str__(self):
    return f"{self.last_name} ({self.first_name})"
  
class PurchaseHistory(models.Model):
  customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='purchase_history')
  pc_model = models.CharField(max_length=100)
  purchase_date = models.DateField()

  def __str__(self):
    return f'{self.pc_model} ()'
