from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from blog.models import Category, Tag, Article


# Register your models here.

class CategoryAdmin(ImportExportModelAdmin):
    class Meta:
        model = Category


admin.site.register(Category, CategoryAdmin)


class TagAdmin(ImportExportModelAdmin):
    class Meta:
        model = Tag


admin.site.register(Tag, TagAdmin)


class ArticleAdmin(ImportExportModelAdmin):
    class Meta:
        model = Article


admin.site.register(Article, ArticleAdmin)
