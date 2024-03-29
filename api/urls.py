from django.urls import path

from .api import get_project_view, get_all_projects_view, get_image_view, send_message_view, get_render_all_view, get_about_view

urlpatterns = [
    path('project.get', get_project_view),
    path('image.get', get_image_view),
    path('project.get_all', get_all_projects_view),
    path('message.send', send_message_view),
    path('render.get_all', get_render_all_view),
    path('about.get', get_about_view),
]
