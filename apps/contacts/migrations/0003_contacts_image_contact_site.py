# Generated by Django 4.1.5 on 2023-01-17 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0002_alter_contacts_email_site'),
    ]

    operations = [
        migrations.AddField(
            model_name='contacts',
            name='image_contact_site',
            field=models.ImageField(default=1, upload_to='contact', verbose_name='Фотография для страницы Контакты'),
            preserve_default=False,
        ),
    ]
