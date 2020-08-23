from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.urls import reverse
from django.contrib import auth
from django.contrib.auth import authenticate
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from .form import LoginForms

# python manage.py createsuperuser


def index(request):
    return HttpResponse('Welcome to XXX Homepage!')


def login_page(request):
    if request.method == 'GET':
        login_form = LoginForms()
        return render(request, 'login_form.html', {'form': login_form})
    elif request.method == 'POST':
        login_form = LoginForms(request.POST)
        if login_form.is_valid():
            cd = login_form.cleaned_data
            user = authenticate(
                username=cd['username'], password=cd['password'])

            if user:
                auth.login(request, user)
                # return HttpResponse('登录成功')
                return HttpResponseRedirect("logined")
            else:
                return HttpResponse('登录失败')


@login_required
def logined_page(request):
    username = request.user.username
    return render(request, 'user_home.html', {"username": username})


def logout(request):
    auth.logout(request)
    # return HttpResponseRedirect(reverse("login_page"))
    return HttpResponseRedirect("login_page")
