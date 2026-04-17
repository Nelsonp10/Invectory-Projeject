from django import forms
from .models import product, oder

class ProductForm(forms.ModelForm):
    class Meta:
        model = product
        fields = ['name', 'category', 'quantity']


class oderForm(forms.ModelForm):
    class Meta:
        model = oder
        fields =['product','order_quantity' ]

