from django.db import models


# Create your models here.
class Publication(models.Model):
    journal_choice = (
        (0, "No"),
        (1, "Yes")
    )

    title = models.CharField(max_length=255)
    authors = models.TextField()
    publication_year = models.DateField(blank=True)
    conf_or_journal_name = models.CharField(max_length=100)
    publisher = models.CharField(max_length=100)
    is_journal = models.IntegerField(choices=journal_choice)
    abstract = models.TextField()
    url = models.URLField(max_length=200)

