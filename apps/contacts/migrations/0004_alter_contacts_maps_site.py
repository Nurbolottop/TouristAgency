# Generated by Django 4.1.5 on 2023-01-17 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0003_contacts_image_contact_site'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacts',
            name='maps_site',
            field=models.URLField(verbose_name='Адрес на карте'),
        ),
    ]