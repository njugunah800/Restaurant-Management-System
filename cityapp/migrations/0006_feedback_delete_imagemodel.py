# Generated by Django 4.0 on 2024-12-04 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cityapp', '0005_imagemodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField()),
                ('message', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
            ],
        ),
        migrations.DeleteModel(
            name='ImageModel',
        ),
    ]
