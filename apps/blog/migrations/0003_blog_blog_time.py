# Generated by Django 4.1.5 on 2023-01-17 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_blog_blog_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='blog_time',
            field=models.DateTimeField(auto_now_add=True,),
            preserve_default=False,
        ),
    ]
