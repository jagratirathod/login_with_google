from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


# pip install social-auth-app-django


def login(request):
    return render(request , "login.html")



@login_required
def home(request):
    return HttpResponse("Login Successfully ... ")




