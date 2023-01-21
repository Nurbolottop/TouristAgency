# Generated by Django 4.1.5 on 2023-01-21 02:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0002_tours_accommodation_tour_tours_comfort_tour_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Имя')),
                ('email', models.EmailField(max_length=254, verbose_name='Почта')),
                ('message', models.TextField(verbose_name='Коментарий')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_comment', to='tours.tours')),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
    ]
