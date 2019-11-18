from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class ImageModel(models.Model):
    url = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.url


class ProjectModel(models.Model):
    name = models.CharField(max_length=100)
    body = models.TextField()
    titleImage = models.ForeignKey(ImageModel, on_delete=models.SET_NULL, null=True, related_name="%(app_label)s_%(class)s_related_title")
    githubUrl = models.CharField(max_length=100)
    images = models.ManyToManyField(ImageModel, related_name="%(app_label)s_%(class)s_related_images")

    def __str__(self):
        return self.name
