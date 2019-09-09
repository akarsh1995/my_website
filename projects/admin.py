from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from projects.models import Project, Contributor


# Register your models here.

class ContributorAdmin(ImportExportModelAdmin):
    class Meta:
        model = Contributor


admin.site.register(Contributor, ContributorAdmin)


class ProjectAdmin(ImportExportModelAdmin):
    class Meta:
        model = Project


admin.site.register(Project, ProjectAdmin)
