from django.db import models
from phone_field import PhoneField


# Create your models here.
class Summary(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=155)
    phone = PhoneField()
    email = models.EmailField()
    overview = models.TextField()


class Education(models.Model):
    degree = models.CharField(max_length=50)
    department = models.CharField(max_length=100)
    school = models.CharField(max_length=100)
    duration = models.CharField(max_length=100)
    school_address = models.CharField(max_length=100)
    thesis_topic = models.TextField(blank=True)


class Experience(models.Model):
    job_title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    company_address = models.CharField(max_length=100)
    start_year = models.CharField(max_length=50)
    end_year = models.CharField(max_length=50)

    def __str__(self):
        return self.job_title


class JobResponsibility(models.Model):
    job_id = models.ForeignKey(Experience, on_delete=models.CASCADE)
    responsibility = models.TextField()
