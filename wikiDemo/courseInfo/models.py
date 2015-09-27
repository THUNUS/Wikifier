from django.db import models

# Create your models here.
class courseVideo(models.Model):
    courseName = models.CharField(max_length = 50)
    videoName = models.CharField(max_length = 50)
    resource_link = models.URLField()
    