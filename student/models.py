from django.db import models
from django.core.validators import EmailValidator
from core.models import CommonClass
class Student(CommonClass):
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    email = models.EmailField(unique=True, validators=[EmailValidator(message="Enter a valid email address.")])
    phone = models.CharField(max_length=15)
    password = models.CharField(max_length=100)
    active = models.BooleanField(default=True)
    verified = models.BooleanField(default=False)
    profile_image = models.ImageField(upload_to='students/profile_pics/', null=True, blank=True)


    def __str__(self):
        return f'{self.fname} {self.lname}'
