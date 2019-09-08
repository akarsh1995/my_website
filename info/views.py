from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse
from django.views import generic
from info.forms import GetInTouchForm
# Create your views here.
from info.models import Profile
from my_website.email import email_templated


class AboutDetailView(generic.TemplateView):
    template_name = 'info/about.html'


class HomePageView(generic.TemplateView):
    template_name = 'info/home.html'


def make_full_url(scheme, host, url=None):
    return f'{scheme}://{host}{url if url else ""}'


class GetInTouchFormView(SuccessMessageMixin, generic.FormView):
    form_class = GetInTouchForm
    template_name = 'info/contact.html'
    success_message = 'Your form has been submit ted successfully.'

    def get_success_url(self):
        context = self.get_email_html_context()
        email_templated(subject='Thanks for connecting with us.',
                        text_template='info/email_templates/contact_response.txt',
                        recipient_list=self.recipient_email,
                        html_template='info/email_templates/contact_response.html',
                        context=context)
        return reverse('contact_url')

    def get_email_html_context(self):
        form = self.get_form()
        if form.is_valid():
            cleaned_data = form.cleaned_data
            email_context = {
                'recipient_name': cleaned_data['name'],
                'title_line_one': 'Thanks for the query.',
                'title_line_two': 'I\'d love to get connected to you',
                'message_para_one': 'This is  It\'s been a pleasure to connect to you.',
                'message_para_two': "I'll respond to your query soon.",
                'image': self.get_full_image_url(),
                'mobile': self.profile.phone,
                'email': self.profile.user.email,
                'linkedin': self.profile.linkedin,
                'facebook': self.profile.facebook,
                'github': self.profile.github,
                'website': self.get_website()
            }
            return email_context
        return None

    @property
    def recipient_email(self):
        form = self.get_form()
        if form.is_valid():
            return [form.cleaned_data['email']]
        return None

    @property
    def profile(self) -> Profile:
        from info.context_processors import get_profile
        return get_profile()

    def get_full_image_url(self):
        host = self.request.get_host()
        scheme = self.request.scheme
        url = self.profile.photo.url
        print(host, scheme, url)
        return make_full_url(scheme, host, url)

    def get_website(self):
        host = self.request.get_host()
        scheme = self.request.scheme
        return make_full_url(scheme, host)
