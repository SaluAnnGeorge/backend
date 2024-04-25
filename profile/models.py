from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    education = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=15)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    interests = models.TextField(blank=True)
    date_of_birth = models.DateField()

    def __str__(self):
        return self.name
