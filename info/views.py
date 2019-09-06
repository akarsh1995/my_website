from django.shortcuts import render
from django.views import generic


# Create your views here.

def about(request):
    return render(request, 'info/about.html')


class HomePageView(generic.TemplateView):
    template_name = 'info/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['personal_details'] = {
            'first_name': 'Akarsh Jain'
        }
        return context


class ContactPageView(generic.TemplateView):
    template_name = 'info/contact.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['personal_details'] = {
            'phone': 8962141060,
            'phone_timings': 'Mon to Fri 9am to 6pm',
            'address': 'Bangalore',
            'street': 'Bomanahalli-560068',
            'email': 'akarsh.1995.02@gmail.com',
            'email_timings': 'Send me query anytime.'
        }
        return context
