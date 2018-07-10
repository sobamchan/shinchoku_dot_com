from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate

from .forms import UserForm


def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = User.objects.create_user(username, '', password)
        user.save()
        return redirect('signin')
    else:
        form = UserForm()
        context = {'form': form}
        return render(request, 'signup.html', context)


def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('shinchoku:index')
    else:
        form = UserForm()
        context = {'form': form}
        return render(request, 'signin.html', context)
