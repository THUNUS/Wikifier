from django.db import models

# Create your models here.
class DemoPost(models.Model):
    forum_name = models.CharField(max_length = 50)
    title = models.CharField(max_length = 150)
    body = models.TextField()
class Struct(models.Model):
    name = models.CharField(max_length = 150)
    code = models.TextField()