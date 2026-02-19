from django import forms
from  .models import profile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm  

class CreateUserForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username','email']


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model= User
        fields = ['username', 'email']


class profileUpdateForm(forms.ModelForm):
    class Meta:
        model = profile
        fields = ['address', 'phone','image']