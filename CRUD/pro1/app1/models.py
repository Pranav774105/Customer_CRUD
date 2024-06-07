from django.db import models

# Create your models here.


class Teacher(models.Model):
    tid = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    sal = models.IntegerField()
    exp = models.DateTimeField()