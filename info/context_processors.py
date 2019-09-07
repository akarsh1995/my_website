from info.views import get_profile


def social_links(request):
    p = get_profile()
    return {
        'social_links': {
            'linkedin': p.linkedin,
            'so': p.stack_overflow,
            'github': p.github,
            'fb': p.facebook
        }
    }