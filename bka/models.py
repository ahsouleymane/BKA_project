from django.db import models

# Create your models here.

class forfait(models.Model):
    nom = models.CharField(max_length=50, null=True)

    def __str__(self):
        return str(self.nom)

class service(models.Model):
    forfait = models.ForeignKey(forfait, null=True, on_delete=models.CASCADE)
    nom_service = models.CharField(max_length=20, null=True)
    nom_produit = models.CharField(max_length=50, null=True)
    debit = models.CharField(max_length=20, null=True)
    volume_jour = models.CharField(max_length=20, null=True)
    volume_nuit = models.CharField(max_length=50, null=True)
    validite = models.CharField(max_length=30, null=True)

    date_ajout = models.DateTimeField(auto_now_add=True)
    date_modif = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.nom_service)
    
class installation_information(models.Model):
    customer = models.CharField(max_length=100, null=True)
    lat = models.FloatField(max_length=20, null=True)
    lon = models.FloatField(max_length=20, null=True)
    status = models.BooleanField(default=False)

    date_ajout = models.DateTimeField(auto_now_add=True)
    date_modif = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.customer) 
    
class validation(models.Model):
    customer = models.ForeignKey(installation_information, null=True, on_delete=models.CASCADE)
    forfait = models.ForeignKey(forfait, null=True, on_delete=models.CASCADE)
    service = models.ForeignKey(service, null=True, on_delete=models.CASCADE)
    activer = models.BooleanField(default=False)

    date_ajout = models.DateTimeField(auto_now_add=True)
    date_modif = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.customer) 

class activation(models.Model):
    information = models.ForeignKey(installation_information, null=True, on_delete=models.CASCADE)
    cle_activation = models.CharField(max_length=100, null=True)

    date_ajout = models.DateTimeField(auto_now_add=True)
    date_modif = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.cle_activation) 
    