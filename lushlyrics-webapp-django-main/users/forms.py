from django import forms
from .models import Account

class RegistrationForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':'Enter Password',
        'class':'form-input'
    }))
    
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':'Confirm Password',  
        'class':'form-input'
    }))
    
    class Meta:
        model = Account
        fields = ['email','password']
        
        widgets = {
            'email':forms.EmailInput(attrs={
                'placeholder':'Enter Email',
                'class':'form-input'
            }),
            
        }
    def clean(self):
        cleaned_data = super(RegistrationForm, self).clean()
        
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')
        
        if password1 != password2:
            raise forms.ValidationError(
                "Password does not match!"
            )
        
class UserLogin(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':'Enter Password',
        'class':'form-control'
    }))
    
    class Meta:
        model = Account
        fields = ['email','password']
        
        widgets = {
            'email':forms.EmailInput(attrs={
                'placeholder':'Enter Email',
                'class':'form-control'
            }),
            
        }
       