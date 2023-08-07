# Generated by Django 3.2 on 2023-08-07 17:40

from django.db import migrations
import phonenumbers

def update_phone_numbers(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    for flat in Flat.objects.all().iterator():
        pure_phone = phonenumbers.parse(flat.owners_phonenumber, 'RU')
        flat.owner_pure_phone = f'{pure_phone.country_code}{pure_phone.national_number}'
        flat.save()



class Migration(migrations.Migration):

    dependencies = [
        ('property', '0008_flat_owner_pure_phone'),
    ]

    operations = [
        migrations.RunPython(update_phone_numbers)
    ]