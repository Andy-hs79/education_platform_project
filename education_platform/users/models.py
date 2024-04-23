from django.db import models


class User(models.Model):
    # id =
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    e_mail = models.CharField(max_length=50)
    password = models.CharField(max_length=20)


# Create your models here.
