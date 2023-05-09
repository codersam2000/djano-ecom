from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

# Create your views here.
def login(request):
    if request.method == 'POST' and request.POST['submit_action'] == 'login':
        username = request.POST['login_username']
        password = request.POST['login_password']
        print(username, password)
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponse('User Login')
        else:
            return HttpResponse('User not found')
    elif request.method == 'POST' and request.POST['submit_action'] == 'signup':
        username = request.POST['signup_name']
        email = request.POST['signup_email']
        password = request.POST['signup_password']
        password2 = request.POST['signup_password2']
        if not username or not email or not password or not password2:
            return HttpResponse('Fill all feiid!')
        elif password != password2:
            return HttpResponse('Password dose not match!')
        elif User.objects.filter(username=username).exists():
            return HttpResponse('Username already exists!')
        elif User.objects.filter(email=email).exists():
            return HttpResponse('Email already exists!')
        else:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            return HttpResponse('User signup')
        return HttpResponse('User Sign Up')
    return render(request,'user/login.html')
