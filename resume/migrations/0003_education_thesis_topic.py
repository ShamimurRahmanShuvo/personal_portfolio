# Generated by Django 4.2.17 on 2025-01-16 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0002_rename_position_experience_job_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='education',
            name='thesis_topic',
            field=models.TextField(blank=True),
        ),
    ]
