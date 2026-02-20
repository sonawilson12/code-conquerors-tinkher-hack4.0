from django.shortcuts import render
from .import models
from django.core.mail import send_mail
from django.conf import settings
import random

# Create your views here.

def index(request):
    return render(request,'index.html')

def register(request):
    if request.method=='POST':
        name=request.POST.get('name')
        age=request.POST.get('age')
        email=request.POST.get('email')
        password=request.POST.get('password')
        image=request.FILES.get('image')
        if models.reg.objects.filter(email=email).exists():
            alert="<script>alert('email is already exist'); window.location.href='/register/';</script>;"
            return HttpResponse(alert)
        else:
            user=models.reg(name=name,age=age,email=email,password=password,image=image)
            user.save()
            return redirect('login')
    else:   
         return render(request, 'register.html')
     
def login(request):
    if request.method == "POST":
        # Step 1: Initial Login Phase
        if 'email' in request.POST and 'password' in request.POST:
            email = request.POST.get('email')
            password = request.POST.get('password')
            try:
                user = models.reg.objects.get(email=email, password=password)
                # Generate OTP
                otp = random.randint(100000, 999999)
                request.session['otp'] = otp
                request.session['email'] = user.email

                # Send OTP via Email
                send_mail(
                    'Your Login OTP',
                    f'Your OTP is {otp}',
                    settings.EMAIL_HOST_USER,
                    [user.email],
                    fail_silently=False,
                )
                return render(request, 'otp.html', {'msg': 'OTP sent to your email.'})
            except models.reg.DoesNotExist:
                msg = "Invalid email or password"
                return render(request, 'login.html', {'msg': msg})

        # Step 2: OTP Verification Phase
        if 'otp' in request.POST:
            otp = request.POST.get('otp')
            if str(request.session.get('otp')) == otp:
                # OTP matches, log the user in
                return redirect('home')
            else:
                return render(request, 'otp.html', {'msg': 'Invalid OTP'})

    return render(request, 'login.html')

def otp(request):
    return render(request,'otp.html')
            
