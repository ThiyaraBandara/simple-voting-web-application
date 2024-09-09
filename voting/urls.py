# voting/urls.py
from django.urls import path
#from django.contrib.auth import views as auth_views
from .views import profile, vote, index, results
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('vote/<int:candidate_id>/', views.vote, name='vote'),
    path('vote_confirmation/<int:candidate_id>/', views.vote_confirmation, name='vote_confirmation'),
    path('results/', views.results, name='results'),
    path('profile/', profile, name='profile'),  # Add this line for user profile


]