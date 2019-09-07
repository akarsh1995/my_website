from django.urls import path

from blog.views import BlogListView, ArticleDetailView

urlpatterns = [
    path('', BlogListView.as_view(), name='blog_url'),
    path('article/<slug:slug>', ArticleDetailView.as_view(), name='single_article_url'),
]
