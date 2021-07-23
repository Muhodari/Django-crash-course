from django.db import models


# Create your models here.
# normal declaration of class

# class Feature:
#     id: int
#     name: str
#     details: str
#     is_true: bool

class Feature(models.Model):
    name = models.CharField(max_length=100)
    detail = models.CharField(max_length=500)

