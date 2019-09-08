from django.urls import path

from blog.views import ArticleListView, ArticleDetailView

urlpatterns = [
    path('', ArticleListView.as_view(), name='blog_url'),
    path('article/<slug:slug>', ArticleDetailView.as_view(), name='single_article_url'),
]
