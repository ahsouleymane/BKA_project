# Generated by Django 4.1.7 on 2023-08-09 17:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bka', '0006_remove_installation_information_service_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='forfait',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_service', models.CharField(max_length=20, null=True)),
                ('nom_produit', models.CharField(max_length=50, null=True)),
                ('debit', models.CharField(max_length=20, null=True)),
                ('volume_jour', models.CharField(max_length=20, null=True)),
                ('volume_nuit', models.CharField(max_length=50, null=True)),
                ('validite', models.CharField(max_length=30, null=True)),
                ('date_ajout', models.DateTimeField(auto_now_add=True)),
                ('date_modif', models.DateTimeField(auto_now=True)),
                ('forfait', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='bka.forfait')),
            ],
        ),
        migrations.RemoveField(
            model_name='installation_information',
            name='forfait_entreprise',
        ),
        migrations.RemoveField(
            model_name='installation_information',
            name='forfait_residentiel',
        ),
        migrations.RemoveField(
            model_name='installation_information',
            name='type_forfait',
        ),
        migrations.DeleteModel(
            name='forfait_entreprise',
        ),
        migrations.DeleteModel(
            name='forfait_residentiel',
        ),
        migrations.AddField(
            model_name='installation_information',
            name='forfait',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='bka.forfait'),
        ),
        migrations.AddField(
            model_name='installation_information',
            name='service',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='bka.service'),
        ),
    ]