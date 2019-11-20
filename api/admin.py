from django.contrib import admin
from api.models import MessageModel, ProjectModel, ImageModel

# Register your models here.
admin.site.register(MessageModel)
admin.site.register(ProjectModel)
admin.site.register(ImageModel)
