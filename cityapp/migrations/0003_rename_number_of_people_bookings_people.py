# Generated by Django 4.0 on 2024-12-02 12:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cityapp', '0002_bookings'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bookings',
            old_name='number_of_people',
            new_name='people',
        ),
    ]
