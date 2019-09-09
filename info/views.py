from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse
from django.views import generic
from info.forms import GetInTouchForm
# Create your views here.


class AboutDetailView(generic.TemplateView):
    template_name = 'info/about.html'


class HomePageView(generic.TemplateView):
    template_name = 'info/home.html'


class GetInTouchFormView(SuccessMessageMixin, generic.FormView):
    form_class = GetInTouchForm
    template_name = 'info/contact.html'
    success_message = 'Your form has been submitted successfully.'

    def get_success_url(self):
        return reverse('contact_url')

    def form_valid(self, form):
        form.save()
        form.send_email_recipient()
        form.send_email_self()
        return super().form_valid(form)
