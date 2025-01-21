# Generated by Django 4.2.17 on 2025-01-20 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publications', '0002_alter_publication_is_journal'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='publication',
            name='publication_date',
        ),
        migrations.AddField(
            model_name='publication',
            name='publication_year',
            field=models.CharField(blank=True, max_length=4),
        ),
        migrations.AlterField(
            model_name='publication',
            name='conf_or_journal_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='publication',
            name='is_journal',
            field=models.CharField(choices=[(0, 'No'), (1, 'Yes')], max_length=2),
        ),
        migrations.AlterField(
            model_name='publication',
            name='title',
            field=models.CharField(max_length=255),
        ),
    ]
