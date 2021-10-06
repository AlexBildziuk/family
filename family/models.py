from django.db import models

class Family(models.Model):
    title = models.CharField(max_length=32)
    content =models.TextField(blank=True)
    photo = models.ImageField(upload_to="photo/")
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)

