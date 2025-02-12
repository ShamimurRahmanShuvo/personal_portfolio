# Generated by Django 4.2.17 on 2025-01-14 03:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_name', models.CharField(max_length=100)),
                ('profile_description', models.TextField()),
                ('profile_image', models.FileField(blank=True, upload_to='profile_image/')),
            ],
        ),
    ]
