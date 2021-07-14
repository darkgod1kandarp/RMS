from django.db import models

# Create your models here
class check(models.Model):
    email = models.EmailField(max_length = 25)
    password = models.CharField(max_length = 25)
    section  = models.CharField(max_length = 25)

class teach(models.Model):
    name = models.CharField(max_length=50)
    file_name = models.CharField(max_length=50)
    pdf= models.FileField(blank =False)
    



