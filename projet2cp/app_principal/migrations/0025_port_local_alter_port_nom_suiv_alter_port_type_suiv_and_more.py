# Generated by Django 4.0.3 on 2022-04-25 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_principal', '0024_alter_port_etat_alter_port_nom_suiv_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='port',
            name='local',
            field=models.CharField(default='magazin', max_length=100),
        ),
        migrations.AlterField(
            model_name='port',
            name='nom_suiv',
            field=models.CharField(default='Non relié', max_length=100, verbose_name="Nom de l'appareil relié"),
        ),
        migrations.AlterField(
            model_name='port',
            name='type_suiv',
            field=models.CharField(choices=[('Prise', 'Prise'), ('Switch', 'Switch'), ("Point d'accés", "Point d'accés"), ('Aucun', 'Aucun'), ('Autre', 'Autre')], default='Aucun', max_length=15, verbose_name="Type de l'appareil relié "),
        ),
        migrations.AlterField(
            model_name='port',
            name='vlan_associe',
            field=models.CharField(default='Non utilisé', max_length=50, verbose_name='VLAN associé'),
        ),
    ]
