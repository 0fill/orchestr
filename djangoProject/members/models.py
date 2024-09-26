from django.db import models

# Create your models here.

class Member(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    instrument = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
