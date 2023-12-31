# Generated by Django 3.2 on 2023-08-07 17:40

from django.db import migrations
from phonenumbers import is_valid_number, parse
from phonenumber_field.phonenumber import PhoneNumber


def update_phone_numbers(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    for flat in Flat.objects.all().iterator():
        phonenumber = flat.owners_phonenumber
        if is_valid_number(parse(phonenumber, 'RU')):
            flat.owner_pure_phone = PhoneNumber.from_string(phonenumber, region='RU')
            flat.save()


def move_backward(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    Flat.objects.all().update(owner_pure_phone=0)


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0008_flat_owner_pure_phone'),
    ]

    operations = [
        migrations.RunPython(update_phone_numbers)
    ]
