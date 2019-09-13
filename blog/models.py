from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from info.mixins import PTagWrapMixin
from .mixins import CropShrinkImageMixin


class Category(models.Model):
    name = models.CharField(max_length=30, unique=True)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=30, unique=True)

    class Meta:
        verbose_name_plural = "Tags"

    def __str__(self):
        return self.name


class Article(PTagWrapMixin, CropShrinkImageMixin, models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, blank=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=64, unique=True)
    tags = models.ManyToManyField(Tag, blank=True)
    background_image = models.ImageField(upload_to='post/%Y/%m/%d')
    slug = models.SlugField(max_length=38, blank=True)
    content = models.TextField()
    short_description = models.CharField(max_length=150, blank=True, null=True)
    updated_on = models.DateField(auto_now=True)
    created_on = models.DateField(auto_now_add=True)
    publish_on = models.DateField()
    list_display = ('title', 'category', 'tags', 'author', 'publish_on', 'created_on', 'updated_on')
    search_fields = ['title', 'byline', 'symbol']
    list_filter = ['publish_on', 'created_on']
    date_hierarchy = 'pub_date'

    def get_slug(self):
        return slugify(self.title)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        # crop image
        self.crop_image('background_image', (750, 375))

        # wrap new line with p tag
        self.wrap_description_p_tag('content')

        # set slug
        if not self.slug or len(self.slug) > 38:
            self.slug = slugify(self.title)
            self.slug = self.slug[:38] if len(self.slug) > 38 else self.slug

        # set short description
        if self.content:
            self.short_description = self.content if len(self.content) < 140 else self.content[:140] + '...'
        super(Article, self).save()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('single_article_url', kwargs={'slug': self.slug})

    class Meta:
        ordering = ['-publish_on']
