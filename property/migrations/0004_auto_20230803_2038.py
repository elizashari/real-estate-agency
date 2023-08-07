# Generated by Django 2.2.24 on 2023-08-03 17:38

from django.db import migrations


NEW_BUILDING_YEAR = 2015


def new_buildings(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    Flat.objects.filter(construction_year__gte=NEW_BUILDING_YEAR).update(new_building=True)


def old_buildings(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    Flat.objects.exclude(construction_year__gte=NEW_BUILDING_YEAR).update(new_building=False)

class Migration(migrations.Migration):

    dependencies = [
        ('property', '0003_flat_new_building'),
    ]

    operations = [
        migrations.RunPython(new_buildings),
        migrations.RunPython(old_buildings),
    ]
