# Generated by Django 4.1.5 on 2023-01-21 14:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0003_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tickets',
            old_name='name_ticket',
            new_name='title',
        ),
    ]