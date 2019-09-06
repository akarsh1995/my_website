"""my_website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from blog.views import BlogListView, ArticleDetailView
from info.views import ContactPageView, about, HomePageView
from projects.views import project_details, projects
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', BlogListView.as_view(), name='blog_url'),
    path('contact/', ContactPageView.as_view(), name='contact_url'),
    path('about/', about, name='about_url'),
    path('', HomePageView.as_view(), name='home_url'),
    path('article/<int:pk>', ArticleDetailView.as_view(), name='single_article_url'),
    path('projects/', projects, name='projects-url'),
    path('project_details/<int:pk>', project_details, name='project-details-url'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
