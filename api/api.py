from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist

from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.serializers import ProjectSerializer, ImageSerializer, ProjectShortSerializer, MessageSerializer, RenderSerializer, AboutSerializer
from api.models import ProjectModel, ImageModel, RenderModel, AboutModel
from rest_framework import status

User = get_user_model()

@api_view(['GET'])
def get_project_view(request):
    projectid = request.query_params.get('id')
    if projectid is None:
        return Response({"error": "You need to specify \"id\" parameter."})
    try:
        project = ProjectModel.objects.get(pk=projectid)
    except ObjectDoesNotExist as e:
        return Response({"error": "Project with this id does not exist."})
    serializer = ProjectSerializer(project)
    return Response(serializer.data)


@api_view(['GET'])
def get_all_projects_view(request):
    serializer = ProjectShortSerializer(ProjectModel.objects.all(), many=True)
    return Response(serializer.data)


@api_view(['GET'])
def send_message_view(request):
    contacts = request.query_params.get('contacts')
    name = request.query_params.get('name')
    message = request.query_params.get('message')
    if (contacts is None) or (name is None) or (message is None):
        return Response({"error": "contacts, name or message are missing."}, status=status.HTTP_400_BAD_REQUEST)
    serializer = MessageSerializer(data={"contacts": contacts, "name": name, "message": message})
    if not serializer.is_valid():
        return Response({"error": "Incorrect fields."}, status=status.HTTP_400_BAD_REQUEST)
    # return Response(None, status=status.HTTP_404_NOT_FOUND)
    serializer.save()
    return Response(1, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def get_image_view(request):
    imageid = request.query_params.get('id')
    if imageid is None:
        return Response({"error": "You need to specify \"id\" parameter."})
    try:
        image = ImageModel.objects.get(pk=imageid)
    except ObjectDoesNotExist as e:
        return Response({"error": "Image with this id does not exist."})
    serializer = ImageSerializer(image)
    return Response(serializer.data)


@api_view(['GET'])
def get_render_all_view(request):
    serializer = RenderSerializer(RenderModel.objects.all(), many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_about_view(request):
    serializer = AboutSerializer(AboutModel.objects.last())
    return Response(serializer.data)
