from django.db import models


class Camera(models.Model):
    name = models.CharField(max_length=100)
    url = models.URLField()
    mime = models.CharField(max_length=100, default="")
    data = models.TextField(default="")
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Image(models.Model):
    name = models.CharField(max_length=100)
    url = models.URLField()

    def __str__(self):
        return self.name
