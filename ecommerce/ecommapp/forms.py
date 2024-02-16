from django import forms
from django.contrib.auth.models import User
from ecommapp.models  import Carts,Orders
 
class UserRegister(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password','email']
        widgets={
            'first_name':forms.TextInput(attrs={'class':'form-control','placeholder':'firstName'}),
            'last_name':forms.TextInput(attrs={'class':'form-control','placeholder':'lastName'}),
            'username':forms.TextInput(attrs={'class':'form-control','placeholder':'userName'}),
            'password':forms.TextInput(attrs={'class':'form-control','placeholder':'password'}),
            'email':forms.TextInput(attrs={'class':'form-control','placeholder':'email'}),
        }
class UserLoggin(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','password']
        widgets={
            'username':forms.TextInput(attrs={'class':'form-control','placeholder':'userName'}),
            'password':forms.TextInput(attrs={'class':'form-control','placeholder':'password'}),

        }

class CartForm(forms.ModelForm):
    class Meta:
        model=Carts
        fields=['quantity']

        widgets={
            'quantity':forms.NumberInput(attrs={'class':'form-control'})
        }
class OrderForm(forms.ModelForm):
    class Meta:
        model=Orders
        fields=['address','mail']
        widgets={
            'address':forms.TextInput(attrs={'class':'form-control'}),
            'mail':forms.EmailInput(attrs={'class':'form-control'})
        } 