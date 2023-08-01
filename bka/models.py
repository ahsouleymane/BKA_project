from django.db import models

# Create your models here.

class installation_information(models.Model):
    forfait = models.ForeignKey(forfait, null=True, on_delete=models.CASCADE)
    customer = models.CharField(max_length=100, null=True)
    lat = models.FloatField(max_length=20, null=True)
    lon = models.FloatField(max_length=20, null=True)
    value = models.FloatField(max_length=8, default=0.0)
    CHOIX = (
        ('Ko', 'Ko'),
        ('Mo', 'Mo'),
        ('Go', 'Go'),
    )
    unit = models.CharField(max_length=10, choices=CHOIX, default='Mo')
    status = models.BooleanField(default=False)

    date_ajout = models.DateTimeField(auto_now_add=True)
    date_modif = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.customer) 
    
class forfait(models.Model):
    forfait_residentiel = models.ForeignKey(forfait_residentiel, null=True, on_delete=models.CASCADE)
    forfait_entreprise = models.ForeignKey(forfait_entreprise, null=True, on_delete=models.CASCADE)
    
class forfait_residentiel(models.Model):
    nom_service = models.CharField(max_length=20, null=True)
    nom_produit = models.CharField(max_length=30, null=True)
    debit = models.CharField(max_length=10, null=True)
    volume_jour = models.IntegerField(max_length=10, null=True)
    volume_nuit = models.CharField(max_length=100, null=True)
    validite = models.CharField(max_length=30, null=True)

    date_ajout = models.DateTimeField(auto_now_add=True)
    date_modif = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.nom_service)
    
class forfait_entreprise(models.Model):
    nom_service = models.CharField(max_length=20, null=True)
    nom_produit = models.CharField(max_length=30, null=True)
    debit = models.CharField(max_length=10, null=True)
    volume = models.CharField(max_length=10, null=True)
    validite = models.CharField(max_length=30, null=True)

    date_ajout = models.DateTimeField(auto_now_add=True)
    date_modif = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.nom_service)

