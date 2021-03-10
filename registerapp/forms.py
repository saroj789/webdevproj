from django.forms import ModelForm
from .models import User
from django import forms

 
  


class regForm(forms.ModelForm):
    
    class Meta:
        model = User 
        fields = "__all__"
        #labels={'userid':"enter userid",'email':"enter email",'passward':"enter passward",'retype_passward':'confirm passward'}
        widgets={'passward':forms.PasswordInput(attrs={'placeholder':'type passsward'}),
                'retype_passward':forms.PasswordInput(attrs={'placeholder':'retype passsward'}),
                'phone_no':forms.NumberInput(attrs={"placeholder": "your mobile number"}),
                #'name': forms.CharField(max_length=20)
               
                } 

class loginForm(forms.ModelForm):
    
    class Meta:
        model = User
        fields = ("userid",'passward')
        widgets={'passward':forms.PasswordInput(attrs={'placeholder':'type passsward'})}




