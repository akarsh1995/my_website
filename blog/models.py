import mimetypes
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
        if not self.slug:
            self.slug = slugify(self.title)
        self.slug = self.slug[:38] if len(self.slug) > 38 else self.slug
        if len(self.content) > 140:
            self.short_description = self.content[:140] + '...'
        else:
            self.short_description = self.content + "..."
        super(Article, self).save()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('single_article_url', kwargs={'slug': self.slug})
