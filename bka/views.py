from django.shortcuts import render, redirect
from .forms import *
from .models import *

# Create your views here.

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
    if information.status == True:
        list = information

    context = {'list': list}
    return render(request, '', context)

