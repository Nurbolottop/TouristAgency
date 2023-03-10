# Generated by Django 4.1.5 on 2023-01-17 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email_site', models.CharField(max_length=255, verbose_name='Почта')),
                ('phone_site', models.CharField(max_length=255, verbose_name='Тел.ном')),
                ('address_site', models.CharField(max_length=255, verbose_name='Адрес')),
                ('maps_site', models.TextField(verbose_name='Адрес на карте')),
                ('instagram_site', models.URLField(blank=True, null=True, verbose_name='Instagram')),
                ('facebook_site', models.URLField(blank=True, null=True, verbose_name='Fcebook')),
                ('youtube_site', models.URLField(blank=True, null=True, verbose_name='Youtube')),
                ('whatsapp_site', models.URLField(blank=True, null=True, verbose_name='WhatsApp')),
            ],
            options={
                'verbose_name': 'Контакт',
                'verbose_name_plural': 'Контакты',
            },
        ),
    ]
