from django.db import models
from datetime import date

# Create your models here.

class Banner(models.Model):
    banner_bg = models.ImageField(upload_to='pics')
    banner_collection_type = models.CharField(max_length=50)
    banner_caption = models.CharField(max_length=50)


class ContactDetails(models.Model):
    cont_address = models.CharField(max_length=100)
    cont_no = models.CharField(max_length=12)
    cont_email = models.EmailField(max_length=70,blank=True)
    cont_locaton = models.CharField(max_length=100)
    cont_map_url = models.CharField(max_length=1000)

class socialIcon(models.Model):

    social_name = models.CharField(max_length=100)
    socail_url = models.CharField(max_length=100)