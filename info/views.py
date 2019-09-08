from django.views import generic
from info.models import Profile
from django.conf import settings
# Create your views here.


def get_profile():
    return Profile.objects.get(user__username=settings.USER_NAME)


class AboutDetailView(generic.DetailView):
    model = Profile
    template_name = 'info/about.html'
    context_object_name = 'profile'

    def get_object(self, queryset=None):
        return get_profile()


class HomePageView(generic.DetailView):
    model = Profile
    template_name = 'info/home.html'
    context_object_name = 'profile'

    def get_object(self, queryset=None):
        return get_profile()


class ContactPageView(generic.DetailView):
    model = Profile
    template_name = 'info/contact.html'
    context_object_name = 'profile'

    def get_object(self, queryset=None):
        return get_profile()
