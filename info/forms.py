from django.forms import ModelForm

from info.models import GetInTouch, Profile
from info.tasks import email_templated


def make_full_url(scheme, host, url=None):
    return f'{scheme}://{host}{url if url else ""}'


class GetInTouchForm(ModelForm):
    class Meta:
        model = GetInTouch
        fields = '__all__'

    def send_email_recipient(self):
        email_templated.delay(subject='Thanks for connecting with us.',
                              text_template='info/email_templates/contact_response.txt',
                              recipient_list=self.recipient_email,
                              html_template='info/email_templates/contact_response.html',
                              context=self.get_email_html_context())

    def get_email_html_context(self):
        email_context = {
            'recipient_name': self.cleaned_data['name'],
            'title_line_one': 'Thanks for the query.',
            'title_line_two': 'I\'d love to get connected to you',
            'message_para_one': 'This is  It\'s been a pleasure to connect to you.',
            'message_para_two': "I'll respond to your query soon.",
            'image': self.profile.photo.url,
            'mobile': self.profile.phone,
            'email': self.profile.user.email,
            'linkedin': self.profile.linkedin,
            'facebook': self.profile.facebook,
            'github': self.profile.github,
            'website': 'http://www.akarsh.tk'
        }
        return email_context

    @property
    def recipient_email(self):
        return [self.cleaned_data['email']]

    @property
    def profile(self) -> Profile:
        from info.context_processors import get_profile
        return get_profile()

    def send_email_self(self):
        email_templated.delay(subject=f'Email from {self.recipient_email[0]}',
                              text_template='info/email_templates/contact_intimation.txt',
                              recipient_list=[self.profile.user.email],
                              context={
                                  'subject': self.cleaned_data['subject'],
                                  'message': self.cleaned_data['message']
                              })
