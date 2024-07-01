from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import SignupForm
from .models import User

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully!')
            return redirect('login')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.user_type == 'Patient':
                return redirect('dashboard_patient')
            else:
                return redirect('dashboard_doctor')
        else:
            messages.error(request, 'Invalid credentials')
    return render(request, 'login.html')

def dashboard_patient(request):
    return render(request, 'dashboard_patient.html')

def dashboard_doctor(request):
    return render(request, 'dashboard_doctor.html')
