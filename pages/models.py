from django.db import models


# Create your models here.
class Profile(models.Model):
    profile_name = models.CharField(max_length=100)
    profile_description = models.TextField()
    profile_image = models.FileField(upload_to="profile_image/", blank=True)
