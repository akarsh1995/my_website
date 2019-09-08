from django.urls import path

from info.views import ContactPageView, AboutDetailView, HomePageView

urlpatterns = [
    path('contact/', ContactPageView.as_view(), name='contact_url'),
    path('about/', AboutDetailView.as_view(), name='about_url'),
    path('', HomePageView.as_view(), name='home_url'),
]

