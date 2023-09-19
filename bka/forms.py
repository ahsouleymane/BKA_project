from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import *

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']

class installation_informationForm(forms.ModelForm):
    class Meta:
        model = installation_information
        fields = ['customer', 'lat', 'lon']
        labels = {
            'customer': 'Customer',
            'lat': 'Latitude',
            'lon': 'Longitude',
        }

class validationForm(forms.ModelForm):
    class Meta:
        model = validation
        fields = ['information', 'forfait', 'service']
        labels = {
            'information': 'Customer',
            'forfait': 'Forfait',
            'service': 'Service',
        }

        def __init__(self, *args, **kwargs):
            super(validationForm,self).__init__(*args, **kwargs)
            self.fields['information'].empty_label = "Choisir"

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['service'].queryset = service.objects.none()

            if 'forfait' in self.data:
                try:
                    forfait_id = int(self.data.get('forfait'))
                    self.fields['service'].queryset = service.objects.filter(forfait_id=forfait_id).order_by('nom_service')
                except (ValueError, TypeError):
                    pass
            elif self.instance.pk:
                self.fields['service'].queryset = self.instance.forfait.service_set.order_by('nom_service')

class activationForm(forms.ModelForm):
    class Meta:
        model = activation
        fields = '__all__'

class ServiceForm(forms.ModelForm):
    class Meta:
        model = service
        fields = ['nom_service', 'nom_produit', 'debit', 'volume_jour', 'volume_nuit', 'validite']
        labels = {
            'nom_service': 'Nom Service',
            'nom_produit': 'Nom Produit',
            'debit': 'Débit',
            'volume_jour': 'Volume Jour',
            'volume_nuit': 'Volume Nuit',
            'validite': 'Validité',
        }
