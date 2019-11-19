from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class ImageModel(models.Model):
    url = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    description = models.TextField()
    titleRu = models.CharField(max_length=100)
    descriptionRu = models.TextField()

    def __str__(self):
        return self.url


class MessageModel(models.Model):
    contacts = models.CharField(max_length=100, blank=False)
    name = models.CharField(max_length=100, blank=False)
    message = models.CharField(max_length=500, blank=False)

    def __str__(self):
        return self.name


class ProjectModel(models.Model):
    name = models.CharField(max_length=100)
    body = models.TextField()
    bodyRu = models.TextField()
    titleImage = models.ForeignKey(ImageModel, on_delete=models.SET_NULL, null=True, related_name="%(app_label)s_%(class)s_related_title")
    githubUrl = models.CharField(max_length=100)
    images = models.ManyToManyField(ImageModel, related_name="%(app_label)s_%(class)s_related_images")

    def __str__(self):
        return self.name
