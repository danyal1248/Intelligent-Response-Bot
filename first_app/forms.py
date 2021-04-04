from django import forms
from django.contrib.auth.models import User
from first_app.models import UserProfileInfo



class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(
    attrs = {
    'class' : 'form-control',
    'id'    : 'email-login',
    'placeholder': 'User Name'

    }

    ))
    password = forms.CharField(widget=forms.PasswordInput(

    attrs = {
    'class' : 'form-control',
    'id'    : 'pwd-login',
    'placeholder': 'Password'

    }

    ))
class UserForm(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username','email','password')
        widgets = {
            'username': forms.TextInput(attrs={'class' : 'form-control',
            'id'    : 'pwd-login'}),
            'email': forms.TextInput(attrs={'class' : 'form-control',
            'id'    : 'pwd-login','placeholder': 'Email'}),
        }

class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('site_portfolio','profile_picture')
