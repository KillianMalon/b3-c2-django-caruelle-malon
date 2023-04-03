# Generated by Django 4.1.7 on 2023-04-02 16:20

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_rename_flightschool_booking_flightschool'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='available',
        ),
        migrations.AddField(
            model_name='booking',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='flightschool',
            name='available',
            field=models.BooleanField(default=True),
        ),
    ]
