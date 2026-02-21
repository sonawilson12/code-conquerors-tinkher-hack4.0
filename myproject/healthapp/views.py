from django.shortcuts import redirect, render
from .import models
from django.core.mail import send_mail
from django.conf import settings
import random

# Create your views here.

def index(request):
    return render(request,'index.html')

from django.shortcuts import render, redirect
from .models import reg

def register(request):
    if request.method == "POST":
        name = request.POST.get('name')
        age = request.POST.get('age')
        email = request.POST.get('email')
        password = request.POST.get('password')
        image = request.FILES.get('image')

        reg.objects.create(
            name=name,
            age=age,
            email=email,
            password=password,
            image=image
        )
        return redirect('login')          # ← better to redirect to 'login' or '/'

    return render(request, 'register.html')
     
from django.shortcuts import render, redirect
from .models import reg

def login_view(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = reg.objects.get(email=email, password=password)
            return render(request, 'home.html', {'user': user})
        except reg.DoesNotExist:
            return render(request, 'login.html', {'error': 'Invalid Email or Password'})

    return render(request, 'login.html')

def home(request):
    return render(request,'home.html')   



# healthapp/views.py
from django.shortcuts import render

def get_roadmap(request):
    if request.method == "POST":
        # Get data from the form (standard POST, not JSON)
        weight = float(request.POST.get('weight', 0))
        height = float(request.POST.get('height', 0))
        age = int(request.POST.get('age', 25))
        goal = request.POST.get('goal', '')

        # Calculations
        bmi = round(weight / ((height/100)**2), 1)
        calories = round((10 * weight) + (6.25 * height) - (5 * age))
        
        if "Chubby" in goal:
            calories += 500
            advice = "Focus on a caloric surplus with strength training."
        else:
            calories -= 500
            advice = "Focus on a caloric deficit and high-intensity cardio."

        # Pass data to the NEW page
        context = {
            'calories': calories,
            'bmi': bmi,
            'advice': advice
        }
        return render(request, 'result.html', context)