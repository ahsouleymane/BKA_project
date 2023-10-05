from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import *
from .models import *

from .decorators import *

from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User

import json as JsonResponse

# Create your views here.

@unauthenticated_user
def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('login_page')
        else:
            messages.info(request, "Nom d'utilisateur / mot de passe incorrect !!!")

    context = {}
    return render(request, 'bka/login.html', context)

def logout_page(request):
    logout(request)
    messages.info(request, 'User logout successfuly !!!')
    return redirect('login_page')

def change_password(request, pk):
    try:
        user = User.objects.get(id=pk)
    except User.DoesNotExist:
        user = None

    if request.method == 'POST':
        o_password = request.POST.get('o_password')
        n_password = request.POST.get('n_password')
        cn_password = request.POST.get('cn_password')

    #if user.password == o_password:

@allowed_users(allowed_roles=['tech'])
@login_required(login_url='login_page')
def add_installation_informations(request):
    form = installation_informationForm()
    if request.POST:
        customer = request.POST['customer']
        form = installation_informationForm(request.POST)
        if form.is_valid():
            customer_existing = installation_information.objects.filter(customer=customer) and installation_information.objects.filter(customer=customer).exists
            if customer_existing:
                messages.info(request, 'Cet.te client.e existe déja !!! veuillez réessayer...')
                context = {'form': form}
                return render(request, 'bka/tech/add_installation_informations.html', context)
            else:
                form.save()
                return redirect('/list_coordinates/')

    context = {'form': form}
    return render(request, 'bka/tech/add_installation_informations.html', context)

@allowed_users(allowed_roles=['DG'])
@login_required(login_url='login_page')
def add_validation(request):
    form = validationForm()
    if request.method == 'POST':
        form = validationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/liste_infos_valides/')
    
    context = {'form': form}
    return render(request, 'bka/dg/validations.html', context)

@allowed_users(allowed_roles=['DG'])
@login_required(login_url='login_page')
def update_validation(request, pk):
    try:
        information = installation_information.objects.get(id=pk)
    except installation_information.DoesNotExist:
        information = None
    
    if information.status == False:
        information.status = True

        try:
            validations = validation.objects.get(id=pk)
        except validation.DoesNotExist:
            validations = None 

        form = validationForm(instance=validations)
        if request.method == 'POST':
            form = validationForm(request.POST, instance=validations)
            if form.is_valid():
                form.save()
                validations.save(update_fields=['status'])
                return redirect('/liste_infos_valides/', id=pk)
    
    context = {'form': form}
    return render(request, 'bka/dg/validations.html', context)

@allowed_users(allowed_roles=['DG'])
@login_required(login_url='login_page')
def load_services(request):
    forfait_id = request.GET.get('forfait_id')
    services = service.objects.filter(forfait_id=forfait_id).all()
    context = {'services': services}
    return render(request, 'bka/dg/services_dropdown_list_options.html', context)
    
@allowed_users(allowed_roles=['DG'])
@login_required(login_url='login_page')
def cancel_validation(request, pk):
    try:
        information = installation_information.objects.get(id=pk)
    except installation_information.DoesNotExist:
        information = None

    if information.status == True:
        if request.method == "POST":
            information.status = False
            information.save(update_fields=['status'])
            return redirect('/liste_informations/')

    context = {'item': information}
    return render(request, 'bka/dg/cancel_validation.html', context)

@allowed_users(allowed_roles=['tech'])
@login_required(login_url='login_page')
def edit_coordinates(request, pk):
    try:
        information = installation_information.objects.get(id=pk)
    except installation_information.DoesNotExist:
        information = None

    if information.status == False:
        form = installation_informationForm(instance=information)
        if request.method == 'POST':
            customer = request.POST['customer']
            form = installation_informationForm(request.POST, instance=information)
            if form.is_valid():
                customer_existing = installation_information.objects.filter(customer=customer) and installation_information.objects.filter(customer=customer).exists
                if customer_existing:
                    messages.info(request, 'Cet.te client.e existe déja !!! veuillez réessayer...')
                    context = {'form': form}
                    return render(request, 'bka/tech/edit_coordinates.html', context)
                else:
                    form.save()
                    return redirect('/list_coordinates/')
        
    context = {'form': form}
    return render(request, 'bka/tech/edit_coordinates.html', context)

@allowed_users(allowed_roles=['tech'])
@login_required(login_url='login_page')
def delete_coordinates(request, pk):
    coordinates = installation_information.objects.get(id=pk)
    if coordinates.status == False:
        if request.method == "POST":
            coordinates.delete()
            return redirect('/list_coordinates/')
    
    context = {'item': coordinates}
    return render(request, 'bka/tech/delete_validation.html', context)

@allowed_users(allowed_roles=['tech'])
@login_required(login_url='login_page')
def list_coordinates(request):
    try:
        list_information = installation_information.objects.all().filter(status=False)
    except installation_information.DoesNotExist:
        list_information = None

    context = {'list': list_information}
    return render(request, 'bka/tech/list_coordinates.html', context)

@allowed_users(allowed_roles=['PMO'])
@login_required(login_url='login_page')
def list_coordinates_pmo(request):
    try:
        list_information = installation_information.objects.all().filter(status=False)
    except installation_information.DoesNotExist:
        list_information = None

    context = {'list': list_information}
    return render(request, 'bka/pmo/list_coordinates_pmo.html', context)

@allowed_users(allowed_roles=['DG'])
@login_required(login_url='login_page')
def liste_informations(request):
    try:
        list_information = installation_information.objects.all()
    except installation_information.DoesNotExist:
        list_information = None

    context = {'list': list_information}
    return render(request, 'bka/dg/liste_informations.html', context)

@allowed_users(allowed_roles=['DG'])
@login_required(login_url='login_page')
def liste_infos_valides(request):
    try:
        list_informations = installation_information.objects.all()
    except installation_information.DoesNotExist:
        list_informations = None

    try:
        list_informations_valides = validation.objects.all()
    except validation.DoesNotExist:
        list_informations_valides = None

    context = {'list_infos': list_informations, 'list_infos_valides': list_informations_valides}
    return render(request, 'bka/dg/liste_infos_valides.html', context)

@allowed_users(allowed_roles=['PMO'])
@login_required(login_url='login_page')
def list_valid_informations_pmo(request):
    try:
        list_valid_information = installation_information.objects.all().filter(status=True)
    except installation_information.DoesNotExist:
        list_valid_information = None

    context = {'list': list_valid_information}
    return render(request, 'bka/pmo/list_valid_informations_pmo.html', context)

@allowed_users(allowed_roles=['tech'])
@login_required(login_url='login_page')
def list_valid_informations(request):
    try:
        list_valid_information = installation_information.objects.all().filter(status=True)
    except installation_information.DoesNotExist:
        list_valid_information = None

    context = {'list': list_valid_information}
    return render(request, 'bka/tech/list_valid_informations.html', context)

