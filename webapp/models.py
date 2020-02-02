from django.db import models

# Create your models here.

class employee(models.Model):
    firstName = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    emp_id = models.IntegerField()

    def __str__(self):
        return self.firstName
