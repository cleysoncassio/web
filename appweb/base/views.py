from django.shortcuts import render, redirect
from django.contrib.auth import (
    authenticate,
    login as app_login,
    logout as app_logout
)
from django.contrib import messages


def home(request):
    return render(request, 'base/home.html')


def novo(request):
    return render(request, 'cliente/list.html')


def login(request):
    return render(request, "base/login.html")


def submit_login(request):
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            app_login(request, user)
            return redirect("base")
        else:
            messages.error(request, "Usuário/Senha Inválidos. Por favor tente novamente")

    return redirect("login")


def logout(request):
    app_logout(request)
    return redirect("login")
