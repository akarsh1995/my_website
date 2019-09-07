from django.urls import path

from projects.views import ProjectDetailView, ProjectListView

urlpatterns = [
    path('', ProjectListView.as_view(), name='projects-url'),
    path('project_details/<slug:slug>', ProjectDetailView.as_view(), name='project-details-url')
]
