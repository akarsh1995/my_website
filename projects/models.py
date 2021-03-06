from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from blog.models import Category
from info.mixins import PTagWrapMixin, KeywordExtractorMixin, clean_html


class Project(KeywordExtractorMixin, PTagWrapMixin, models.Model):
    creator = models.ForeignKey(User, related_name='projects', on_delete=models.CASCADE)
    title = models.CharField(max_length=150, blank=True)
    category = models.ForeignKey(Category, blank=True, null=True, related_name='projects', on_delete=models.PROTECT)
    start_date = models.DateField(blank=True)
    end_date = models.DateField(blank=True, null=True, help_text='If currently working leave as it is')
    url = models.URLField(blank=True, null=True)
    description = models.TextField(blank=True)
    currently_working = models.BooleanField()
    slug = models.CharField(max_length=100, blank=True)
    display_image = models.ImageField(blank=True, null=True, upload_to='projects/')
    keywords = models.TextField(blank=True, null=True)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        self.wrap_description_p_tag('description')
        if not self.slug or len(self.slug) > 100:
            self.slug = slugify(self.title)
            if len(self.slug) > 100:
                self.slug = self.slug[:100]

        # keywords
        if not self.keywords:
            self.keywords = self.get_keywords('description')
        super(Project, self).save()

    class Meta:
        verbose_name_plural = 'Projects'
        ordering = ['-end_date']

    def get_absolute_url(self):
        return reverse('project-details-url', kwargs={'slug': self.slug})

    @property
    def meta_description(self):
        cleaned_description = clean_html(self.description)
        return cleaned_description if len(cleaned_description) < 140 else cleaned_description[:140]

    def __str__(self):
        return self.title


class Contributor(models.Model):
    project = models.ForeignKey(Project, null=True, blank=True, related_name='contributors', on_delete=models.CASCADE)
    name = models.CharField(max_length=25, null=True, blank=True)
    linkedin = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.name
