from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from .models import UserProfile
import re

User = get_user_model()  # This will get the custom user model if you have one

class SignupForm(UserCreationForm):
    nic_number = forms.CharField(
        max_length=150,
        help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.',
        label='NIC Number'
    )
    password1 = forms.CharField(widget=forms.PasswordInput, label='Password')
    password2 = forms.CharField(widget=forms.PasswordInput, label='Confirm Password')
    

    class Meta:
        model = User
        fields = ['nic_number', 'password1', 'password2']  # username will be National ID number

    def clean_username(self):
        username = self.cleaned_data.get('username')

        # Check if username is alphanumeric
        if not re.match(r'^[A-Za-z0-9]+$', username):
            raise ValidationError("Username must only contain letters and numbers.")
        
        # Check if username is unique
        if User.objects.filter(username=username).exists():
            raise ValidationError("A user with this National ID number already exists.")
        return username

    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')
        
        # Validate password strength
        if not re.match(r'^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$', password1):
            raise ValidationError("Password must be at least 8 characters long and include at least one letter, one number, and one special character.")
        return password1

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['bio', 'profile_picture']