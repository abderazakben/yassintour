# Generated by Django 3.2.5 on 2021-07-10 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_admin'),
    ]

    operations = [
        migrations.AddField(
            model_name='excursions',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
