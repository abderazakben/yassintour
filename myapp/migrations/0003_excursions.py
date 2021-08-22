# Generated by Django 3.2.5 on 2021-07-08 01:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_rename_a_address_activities_address'),
    ]

    operations = [
        migrations.CreateModel(
            name='Excursions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address_E', models.CharField(max_length=200, null=True)),
                ('image_E', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('Text_E', models.TextField(max_length=600)),
                ('price_E', models.IntegerField(blank=True, null=True)),
                ('date_E', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ('address_E',),
            },
        ),
    ]
