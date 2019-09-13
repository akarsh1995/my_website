from django.views import generic
from projects.models import Project


class ProjectListView(generic.ListView):
    model = Project
    context_object_name = 'projects'
    template_name = 'projects/projects.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        ctx = super().get_context_data()
        ctx['category'] = self.request.GET.get('category')
        return ctx

    def get_queryset(self):
        if self.request.GET.get('category'):
            return Project.objects.filter(category__name=self.request.GET.get('category'))
        return super().get_queryset()


class ProjectDetailView(generic.DetailView):
    template_name = 'projects/project_details.html'
    model = Project
    context_object_name = 'project'
