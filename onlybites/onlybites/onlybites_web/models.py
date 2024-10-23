from django.db import models

class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=75)
    surname = models.CharField(max_length=75)
    birthdate = models.DateTimeField()
    mail = models.CharField(max_length=75)
    telephone = models.CharField(max_length=75)


