# Generated by Django 4.0.3 on 2022-04-05 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_principal', '0015_modeleswitch_nom'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vlan',
            name='num_Vlan',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
