# Generated by Django 4.1.7 on 2023-08-15 16:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bka', '0008_alter_installation_information_forfait'),
    ]

    operations = [
        migrations.AlterField(
            model_name='installation_information',
            name='forfait',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to='bka.forfait'),
        ),
    ]
