# Generated by Django 4.1.5 on 2023-01-17 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Slide',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name_slide', models.CharField(max_length=255, verbose_name='Название первого слайда')),
                ('first_description_slide', models.TextField(verbose_name='Описание первого слайда')),
                ('second_name_slide', models.CharField(max_length=255, verbose_name='Название второго слайда')),
                ('second_description_slide', models.TextField(verbose_name='Описание второго слайда')),
            ],
            options={
                'verbose_name': 'Слайд',
                'verbose_name_plural': 'Слайды',
            },
        ),
    ]
