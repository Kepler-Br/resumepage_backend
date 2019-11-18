from rest_framework import serializers
from api.models import ImageModel, ProjectModel


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageModel
        fields = '__all__'


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectModel
        fields = '__all__'


class ProjectShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectModel
        fields = ['name', 'id']
