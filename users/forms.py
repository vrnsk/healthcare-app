from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class SignupForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = [
            'username', 'first_name', 'last_name', 'profile_picture',
            'email', 'password1', 'password2', 'address_line1',
            'city', 'state', 'pincode', 'user_type'
        ]
