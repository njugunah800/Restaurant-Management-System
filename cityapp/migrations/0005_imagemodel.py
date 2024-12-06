# Generated by Django 4.0 on 2024-12-04 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cityapp', '0004_member'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImageModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('occupation', models.CharField(blank=True, max_length=255, null=True)),
                ('rating', models.PositiveIntegerField()),
                ('message', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
