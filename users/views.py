from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import CompanyProfile

def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('dashboard')
        messages.error(request, 'Invalid credentials')
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def dashboard_view(request):
    try:
        profile = CompanyProfile.objects.get(user=request.user)
    except CompanyProfile.DoesNotExist:
        profile = None
    return render(request, 'dashboard.html', {'profile': profile})

@login_required
def company_profile_view(request):
    try:
        profile = CompanyProfile.objects.get(user=request.user)
    except CompanyProfile.DoesNotExist:
        profile = CompanyProfile(user=request.user)

    if request.method == 'POST':
        profile.company_name = request.POST.get('company_name')
        profile.address = request.POST.get('address')
        profile.subscription_plan = request.POST.get('subscription_plan')
        profile.save()
        messages.success(request, 'Profile updated successfully.')
        return redirect('company_profile')

    return render(request, 'company_profile.html', {'profile': profile})
