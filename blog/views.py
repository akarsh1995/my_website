from django.views import generic

from blog.models import Article


# Create your views here.

class ArticleListView(generic.ListView):
    template_name = 'blog/blog.html'
    model = Article
    queryset = Article.objects.all()
    paginate_by = 10
    context_object_name = 'article_list'
    ordering = ['publish_on']


class ArticleDetailView(generic.DetailView):
    model = Article
    template_name = 'blog/article.html'
    context_object_name = 'article'
    queryset = Article.objects.all()
