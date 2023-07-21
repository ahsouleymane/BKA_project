from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import *
from .models import *

from .decorators import unauthenticated_user

# Create your views here.

@unauthenticated_user
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username / password is incorrect !!!')

    context = {}
    return render(request, 'bka/login.html', context)

def logout(request):
    logout(request)
    messages.info(request, 'User logout successfuly !!!')
    return redirect('login')

def add_installation_information(request):
    form = installation_informationForm()
    if request.method == 'POST':
        form = installation_informationForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    context = {'form': form}
    return render(request, '', context)

def edit_installation_information(request, pk):
    try:
        information = installation_information.objects.get(id=pk)
    except installation_information.DoesNotExist:
        information = None

    if information.status == False:
        information.status = True
        form = installation_informationForm(instance=information)
        if request.method == 'POST':
            form = installation_informationForm(request.POST, instance=information)
            if form.is_valid():
                form.save()
            return redirect('/')
        
    context = {'form': form}
    return render(request, '', context)

def list_coordinates(request, pk):
    try:
        information = installation_information.objects.get(id=pk)
    except installation_information.DoesNotExist:
        information = None

    list = []
    # if status == False, only half-empty fields will be displayed
    if information.status == False:
        list = information

    context = {'list': list}
    return render(request, '', context)

def list_all_informations(request, pk):
    try:
        information = installation_information.objects.get(id=pk)
    except installation_information.DoesNotExist:
        information = None

    list = []
    # if status == true, only complete fields will be displayed
    if information.status == True:
        list = information

    context = {'list': list}
    return render(request, '', context)

