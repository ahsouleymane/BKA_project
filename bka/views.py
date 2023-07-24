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
            return redirect('list_coordinates')
        else:
            messages.info(request, "Nom d'utilisateur / mot de passe incorrect !!!")

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
        return redirect('/list_coordinates/')
    context = {'form': form}
    return render(request, 'bka/add_installation_information.html', context)

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

def list_coordinates(request):
    try:
        list_information = installation_information.objects.all().filter(status=False)
    except installation_information.DoesNotExist:
        list_information = None

    context = {'list': list_information}
    return render(request, 'bka/list_coordinates.html', context)

def list_all_informations(request, pk):
    try:
        list_information = installation_information.objects.all().filter(status=True)
    except installation_information.DoesNotExist:
        list_information = None

    context = {'list': list_information}
    return render(request, 'bka/list_all_informations.html', context)

