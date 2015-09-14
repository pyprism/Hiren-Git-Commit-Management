from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages
# Create your views here.


def index(request):
    return render(request, 'index.html')


def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        if user:
            auth.login(request, user)
            return redirect('/hiren')
        else:
            messages.error(request, 'Username/Password is not valid!')
            return redirect(request.path)
    else:
        return redirect('/')