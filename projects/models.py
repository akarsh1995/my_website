from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils.text import slugify

from info.mixins import PTagWrapMixin


class Project(PTagWrapMixin, models.Model):
    creator = models.ForeignKey(User, related_name='projects', on_delete=models.CASCADE)
    title = models.CharField(max_length=150, blank=True)
    start_date = models.DateField(blank=True)
    end_date = models.DateField(blank=True, help_text='If currently working leave as it is')
    url = models.URLField(blank=True, null=True)
    description = models.TextField(blank=True)
    currently_working = models.BooleanField()
    slug = models.CharField(max_length=100, blank=True)
    display_image = models.ImageField(blank=True, upload_to='projects/')

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        self.wrap_description_p_tag('description')
        if not self.slug or len(self.slug) > 100:
            self.slug = slugify(self.title)
            if len(self.slug) > 100:
                self.slug = self.slug[:100]
        super(Project, self).save()

    class Meta:
        verbose_name_plural = 'Projects'

    def get_absolute_url(self):
        return reverse('project-details-url', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title


class Contributor(models.Model):
    project = models.ForeignKey(Project, null=True, blank=True, related_name='contributors', on_delete=models.CASCADE)
    name = models.CharField(max_length=25, null=True, blank=True)
    linkedin = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.name
