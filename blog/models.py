import mimetypes
from urllib.request import urlopen

from django.conf import settings
from django.utils.text import slugify
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


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


class Article(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, blank=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=64, unique=True)
    tags = models.ManyToManyField(Tag, blank=True)
    background_image = models.ImageField(upload_to='post/%Y/%m/%d')
    slug = models.SlugField(max_length=128, blank=True)
    content = models.TextField()
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
        if not self.slug:
            self.slug = self.get_slug()
        super(Article, self).save()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('single_article_url', kwargs={'slug': self.slug})
