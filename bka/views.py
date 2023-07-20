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
