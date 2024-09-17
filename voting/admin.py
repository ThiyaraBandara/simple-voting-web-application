from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Candidate, Vote, CustomUser


# Register your models here.


admin.site.register(Candidate)
admin.site.register(Vote)

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    # Define additional fields and settings if needed

admin.site.register(CustomUser, CustomUserAdmin)

