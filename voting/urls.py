from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('vote/<int:candidate_id>/', views.vote, name='vote'),
    path('vote_confirmation/<int:candidate_id>/', views.vote_confirmation, name='vote_confirmation'),  # New URL for confirmation
    path('results/', views.results, name='results'), 
]