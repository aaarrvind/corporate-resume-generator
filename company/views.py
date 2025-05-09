from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import CompanyProfile
from .forms import CompanyProfileForm

def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('dashboard')
        messages.error(request, "Invalid credentials")
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def dashboard(request):
    try:
        profile = CompanyProfile.objects.get(user=request.user)
    except CompanyProfile.DoesNotExist:
        messages.error(request, "No company profile found. Please create one.")
        return redirect('company_profile')  # Redirect to company profile creation page
    
    return render(request, 'dashboard.html', {'profile': profile})

@login_required
def company_profile(request):
    try:
        profile = CompanyProfile.objects.get(user=request.user)
    except CompanyProfile.DoesNotExist:
        profile = None  # No profile found, allow creating a new one

    if request.method == 'POST':
        if profile:
            form = CompanyProfileForm(request.POST, instance=profile)
        else:
            form = CompanyProfileForm(request.POST)
        
        if form.is_valid():
            new_profile = form.save(commit=False)  # Save without committing to the database yet
            new_profile.user = request.user  # Set the user field to the logged-in user
            profile.usage_count += 1
 
            new_profile.save()  # Now save the instance to the database

            messages.success(request, "Profile updated" if profile else "Profile created")
            return redirect('dashboard')
    else:
        form = CompanyProfileForm(instance=profile if profile else None)
    
    return render(request, 'profile.html', {'form': form})
