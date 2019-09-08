from django.conf import settings

from info.models import Profile


def get_profile():
    return Profile.objects.get(user__username=settings.USER_NAME)


def profile(request):
    p = get_profile()
    return {
        'profile': p
    }
