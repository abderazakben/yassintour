# Generated by Django 3.2.5 on 2021-08-20 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0017_rename_user_cart_costemer2'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='mobile',
            new_name='namber_room',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='order_by',
            new_name='order_name',
        ),
        migrations.RemoveField(
            model_name='order',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='order',
            name='email',
        ),
        migrations.RemoveField(
            model_name='order',
            name='shipping_address',
        ),
        migrations.AddField(
            model_name='order',
            name='Date_dipart',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
    ]
