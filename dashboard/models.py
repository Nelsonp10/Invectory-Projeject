from django.db import models
from django.contrib.auth.models import User

# Create your models here.
CATEGORY = [
    ('Electronic', 'Electronic'),
    ('Stationary', 'Stationary'),
    ('Food', 'Food')

]

class product(models.Model):
    name = models.CharField(max_length=100, null=True)
    category = models.CharField(max_length=20, choices=CATEGORY, null=True)
    quantity = models.PositiveBigIntegerField(null=True)  

    class Meta:
        verbose_name_plural='Product'     
    def __str__(self):
        
     return f'{self.name}- {self.category}- {self.quantity}'   


class oder(models.Model):
    product = models.ForeignKey(product, on_delete=models.CASCADE, null=True)
    staff = models.ForeignKey(User, models.CASCADE, null=True)
    order_quantity = models.PositiveBigIntegerField(null=True)
    order_date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural= 'Order'
    
    def __str__(self):
        return f'{self.product} odered by {self.staff.username} on {self.order_date}'
