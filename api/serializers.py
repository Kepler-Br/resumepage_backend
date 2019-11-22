from rest_framework import serializers
from api.models import ImageModel, ProjectModel, MessageModel, RenderModel


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageModel
        fields = '__all__'


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectModel
        fields = '__all__'


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = MessageModel
        fields = '__all__'


class RenderSerializer(serializers.ModelSerializer):
    class Meta:
        model = RenderModel
        fields = '__all__'
        depth = 1


class ProjectShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectModel
        fields = ['name', 'id', 'titleImage']
