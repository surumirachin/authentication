
import datetime
from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=60)
    description = models.CharField(max_length=200,default='')
    date=models.DateField()
    attachment = models.FileField(upload_to="media/",blank=True,null=True)

    def __str__(self):
        return self.title


