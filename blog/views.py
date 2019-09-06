from django.views import generic

from blog.models import Article


# Create your views here.

class BlogListView(generic.ListView):
    template_name = 'blog/blog.html'
    model = Article
    queryset = Article.objects.all()
    paginate_by = 10


class ArticleDetailView(generic.DetailView):
    model = Article
    template_name = 'blog/article.html'