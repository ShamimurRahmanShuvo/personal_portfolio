from django.db import models
from phone_field import PhoneField


# Create your models here.
class Biography(models.Model):
    job_title = models.CharField(max_length=155)
    employer_name = models.CharField(max_length=100)
    office_name = models.CharField(max_length=100, blank=True)
    education = models.CharField(max_length=100)
    current_city = models.CharField(max_length=50)
    phone_no = PhoneField()
    email = models.EmailField()
    bio = models.TextField()
    profile_image = models.FileField(upload_to="about/", blank=True)


class Skill(models.Model):
    skill_name = models.CharField(max_length=50)
    skill_percentage = models.DecimalField(max_digits=8, decimal_places=2)
