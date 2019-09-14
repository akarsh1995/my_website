from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from info import models


class ExperienceAdmin(ImportExportModelAdmin):
    class Meta:
        model = models.Experience


admin.site.register(models.Experience, ExperienceAdmin)


class ProfileAdmin(ImportExportModelAdmin):
    class Meta:
        model = models.Profile


admin.site.register(models.Profile, ProfileAdmin)


class ClientAdmin(ImportExportModelAdmin):
    class Meta:
        model = models.Client


admin.site.register(models.Client, ClientAdmin)


class PhilosophyAdmin(ImportExportModelAdmin):
    class Meta:
        model = models.Philosophy


admin.site.register(models.Philosophy, PhilosophyAdmin)


class GetInTouchAdmin(ImportExportModelAdmin):
    class Meta:
        model = models.GetInTouch


admin.site.register(models.GetInTouch, GetInTouchAdmin)


class AchievementAdmin(ImportExportModelAdmin):
    class Meta:
        model = models.Achievement


admin.site.register(models.Achievement, AchievementAdmin)
