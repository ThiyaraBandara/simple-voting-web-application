# voting/models.py

from django.db import models
from django.contrib.auth.models import User, AbstractUser, Group, Permission
from django.conf import settings

class Candidate(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Vote(models.Model):
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Vote for {self.candidate.name}'

class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profiles/', blank=True)
    date_of_birth = models.DateField(null=True, blank=True)  # New field for date of birth
    phone_number = models.CharField(max_length=15, blank=True)  # New field for phone number
    address = models.CharField(max_length=255, blank=True)  # New field for address
    created_at = models.DateTimeField(auto_now_add=True)  # New field for creation timestamp
    last_updated = models.DateTimeField(auto_now=True)  # New field for last updated timestamp

    def __str__(self):
        return f'Profile of {self.user.username}'
    
class CustomUser(AbstractUser):
    nic_number = models.CharField(max_length=12, unique=True)

    # Add related_name to avoid conflicts
    groups = models.ManyToManyField(
        Group,
        related_name='customuser_set',
        blank=True,
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='customuser_set',
        blank=True,
    )