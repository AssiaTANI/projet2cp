# Generated by Django 4.0.3 on 2022-04-25 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_principal', '0025_port_local_alter_port_nom_suiv_alter_port_type_suiv_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='switch',
            name='vlans',
            field=models.CharField(blank=True, default='/ ', max_length=350, verbose_name='VLANs associés'),
        ),
    ]
