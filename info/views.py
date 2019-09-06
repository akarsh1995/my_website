from django.shortcuts import render
from django.views import generic
from info.models import Profile
from django.conf import settings
# Create your views here.


def about(request):
    return render(request, 'info/about.html')


def get_profile():
    return Profile.objects.get(user__username=settings.USER_NAME)


class HomePageView(generic.DetailView):
    template_name = 'info/home.html'
    context_object_name = 'profile'

    def get_object(self, queryset=None):
        return get_profile()


class ContactPageView(generic.DetailView):
    template_name = 'info/contact.html'
    context_object_name = 'profile'

    def get_object(self, queryset=None):
        return get_profile()
