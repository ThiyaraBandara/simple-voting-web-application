# voting/models.py

from django.db import models
from django.contrib.auth.models import User

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
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profiles/', blank=True)

    def __str__(self):
        return f'Profile of {self.user.username}'