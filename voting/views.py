from django.shortcuts import render, redirect, get_object_or_404
from .models import Candidate, Vote

def index(request):
    candidates = Candidate.objects.all()
    return render(request, 'voting/index.html', {'candidates': candidates})

def vote(request, candidate_id):
    if request.method == 'POST':
        candidate = get_object_or_404(Candidate, id=candidate_id)
        Vote.objects.create(candidate=candidate)
        return redirect('results')  # Redirect to results page after voting

def results(request):
    candidates = Candidate.objects.all()
    votes = {candidate: Vote.objects.filter(candidate=candidate).count() for candidate in candidates}
    return render(request, 'voting/results.html', {'votes': votes})