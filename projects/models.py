from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.text import slugify


class Project(models.Model):
    creator = models.ForeignKey(User, related_name='projects', on_delete=models.CASCADE)
    title = models.CharField(max_length=150, blank=True)
    start_date = models.DateField(blank=True)
    end_date = models.DateField(blank=True, help_text='If currently working leave as it is')
    url = models.URLField(blank=True, null=True)
    description = models.TextField(blank=True)
    currently_working = models.BooleanField()
    slug = models.CharField(max_length=100, blank=True)
    display_image = models.ImageField(blank=True)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if self.description:
            text_p_wrapped = [f'<p>{line.strip()}</p>' for line in self.description.split('\n') if line and not line.startswith('<')]
            self.description = ''.join(text_p_wrapped)
        if not self.slug:
            self.slug = slugify(self.title)
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
