# voting/forms.py
from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import UserProfile
import re

class UserSignupForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password']  # username will be National ID number

    def clean_username(self):
        username = self.cleaned_data.get('username')

        # Check if username is alphanumeric
        if not re.match(r'^[A-Za-z0-9]+$', username):
            raise ValidationError("Username must only contain letters and numbers.")
        
        # Check if username is unique
        if User.objects.filter(username=username).exists():
            raise ValidationError("A user with this National ID number already exists.")
        else:
         return username

    def clean_password(self):
        password = self.cleaned_data.get('password')
        
        # Validate password strength
        if not re.match(r'^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$', password):
            raise ValidationError("Password must be at least 8 characters long and include at least one letter, one number, and one special character.")
        else:
         return password

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['bio', 'profile_picture']

        # Remove default error messages for username field
        error_messages = {
            'username': {
                'required': {
                    'message': '',  # Remove default required message
                },
            },
        }