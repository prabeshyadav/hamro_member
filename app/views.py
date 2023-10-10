# accounts/views.py

import random
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import CustomUserCreationForm

def register_user(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            # Generate and send OTP
            otp = str(random.randint(100000, 999999))  # Generate a 6-digit OTP
            email = form.cleaned_data['email']

            subject = 'Your OTP Code'
            message = f'Your OTP code is: {otp}'
            from_email = 'youremail@gmail.com'  # Replace with your email
            recipient_list = [email]

            try:
                send_mail(subject, message, from_email, recipient_list)
                request.session['otp'] = otp  # Store the OTP in the session
                request.session['user_data'] = form.cleaned_data  # Store the user registration data
                messages.success(request, 'OTP sent successfully!')
                return redirect('verify_otp')
            except Exception as e:
                messages.error(request, f'Failed to send OTP: {e}')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})







# accounts/views.py

def verify_otp(request):
    if request.method == 'POST':
        entered_otp = request.POST.get('otp')
        stored_otp = request.session.get('otp')  # Get the stored OTP from the session

        if entered_otp == stored_otp:
            user_data = request.session.get('user_data')  # Get the user registration data
            form = CustomUserCreationForm(user_data)  # Create the user using the form data
            if form.is_valid():
                user = form.save()
                login(request, user)  # Log in the user
                del request.session['otp']  # Remove OTP from session
                del request.session['user_data']  # Remove user registration data from session
                messages.success(request, 'Registration successful!')
                return redirect('home')  # Replace 'home' with your desired success URL
            else:
                messages.error(request, 'Invalid registration data. Please try again.')
        else:
            messages.error(request, 'Invalid OTP. Please try again.')

    return render(request, 'registration/verify_otp.html')






from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .forms import LoginForm

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Replace 'home' with your desired success URL
            else:
                form.add_error(None, 'Invalid email or password. Please try again.')
    else:
        form = LoginForm()
    return render(request, 'registration/login.html', {'form': form})
