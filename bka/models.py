from django.db import models

# Create your models here.

class installation_information(models.Model):
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
    

