# Generated by Django 2.2.24 on 2023-08-03 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0005_complain'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complain',
            name='text',
            field=models.TextField(blank=True, null=True, verbose_name='Текст жалобы'),
        ),
    ]