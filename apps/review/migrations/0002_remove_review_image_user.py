# Generated by Django 4.1.5 on 2023-01-20 14:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='image_user',
        ),
    ]