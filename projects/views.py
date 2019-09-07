from django.views import generic
from projects.models import Project


class ProjectListView(generic.ListView):
    model = Project
    context_object_name = 'projects'
    template_name = 'projects/projects.html'


class ProjectDetailView(generic.DetailView):
    template_name = 'projects/project_details.html'
    model = Project
    context_object_name = 'project'
