# voting/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm 
from .models import Candidate, Vote,UserProfile
from .forms import UserSignupForm,UserProfileForm

def index(request):
    candidates = Candidate.objects.all()
    return render(request, 'voting/index.html', {'candidates': candidates})
def signup(request):
    if request.method == 'POST':
        form = UserSignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)  # Log the user in after signup
            return redirect('index')  # Redirect to the index after signup
    else:
        form = UserSignupForm()
    return render(request, 'voting/signup.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('index')
    else:
        form = AuthenticationForm()
    return render(request, 'voting/login.html', {'form': form})



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




