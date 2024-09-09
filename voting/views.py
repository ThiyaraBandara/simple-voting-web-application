# voting/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import Candidate, Vote,UserProfile
from .forms import UserProfileForm

def index(request):
    candidates = Candidate.objects.all()
    return render(request, 'voting/index.html', {'candidates': candidates})

def vote(request, candidate_id):
    if request.method == 'POST':
        candidate = get_object_or_404(Candidate, id=candidate_id)

        # Create the vote without checking for duplicates
        Vote.objects.create(candidate=candidate)
        return redirect('vote_confirmation', candidate_id=candidate.id)  # Redirect to confirmation page

def vote_confirmation(request, candidate_id):
    candidate = get_object_or_404(Candidate, id=candidate_id)
    return render(request, 'voting/vote_confirmation.html', {'candidate': candidate})

def results(request):
    candidates = Candidate.objects.all()
    votes = {candidate: Vote.objects.filter(candidate=candidate).count() for candidate in candidates}
    return render(request, 'voting/results.html', {'votes': votes})

@login_required
def profile(request):
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('profile')  # Redirect to the same page after saving
    else:
        form = UserProfileForm(instance=user_profile)

    return render(request, 'voting/profile.html', {'form': form, 'user_profile': user_profile})

