from django.db import models
from django.contrib.auth.models import User

COUNTRY_CODES = [
    ('+91', 'INDIA')
]


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    about_me = models.TextField(max_length=300)
    country_code = models.CharField(max_length=4, choices=COUNTRY_CODES, blank=True)
    phone = models.IntegerField(blank=True)
    phone_timings = models.CharField(max_length=50)
    city = models.CharField(max_length=30, blank=True)
    street = models.CharField(max_length=40, blank=True)
    email_timings = models.CharField(max_length=50)
    experience_years = models.IntegerField(blank=True)
    linkedin = models.URLField(blank=True)
    github = models.URLField(blank=True)
    stack_overflow = models.URLField(blank=True)
    facebook = models.URLField(blank=True)
    photo = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.user.first_name


class Experience(models.Model):
    profile = models.ForeignKey(Profile,
                                related_name='experiences', on_delete=models.CASCADE)
    designation = models.CharField(max_length=100)
    from_date = models.DateField()
    to_date = models.DateField()
    company = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = 'Experiences'

    def __str__(self):
        return "{}@{}".format(self.designation, self.company)


class Client(models.Model):
    profile = models.ForeignKey(Profile, related_name='clients', on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    designation = models.CharField(max_length=50)
    recommendation = models.TextField()
    image = models.ImageField(blank=True)
    linkedin = models.URLField(blank=True)

    class Meta:
        verbose_name_plural = 'Clients'

    def __str__(self):
        return f'{self.profile}_{self.name}'


class Philosophy(models.Model):
    profile = models.OneToOneField(Profile, related_name='philosophy', on_delete=models.CASCADE)
    title = models.CharField(max_length=150, blank=True)
    description = models.TextField(blank=True)
    image = models.ImageField(blank=True, null=True)

    def __str__(self):
        return f'Philosophy {self.profile}'

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if self.description:
            text_p_wrapped = [f'<p>{line.strip()}</p>' for line in self.description.split('\n') if line]
            self.description = ''.join(text_p_wrapped)
        super(Philosophy, self).save()

    class Meta:
        verbose_name_plural = 'philosophies'


class GetInTouch(models.Model):
    name = models.CharField(max_length=35, null=True, blank=True)
    message = models.TextField(max_length=500, null=True, blank=True)
    email = models.EmailField(max_length=30, null=True, blank=True)
    subject = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f'Message from {self.email}'
