from django.shortcuts import render


# Create your views here.

def projects(request):
    return render(request, 'projects/projects.html')


def project_details(request):
    return render(request, 'projects/project_details.html')
