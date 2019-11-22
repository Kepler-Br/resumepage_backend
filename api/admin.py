from django.contrib import admin
from api.models import MessageModel, ProjectModel, ImageModel, RenderModel

# Register your models here.
admin.site.register(MessageModel)
admin.site.register(ProjectModel)
admin.site.register(ImageModel)
admin.site.register(RenderModel)
