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


class Experience(models.Model):
    profile = models.ForeignKey(Profile,
                                related_name='experiences', on_delete=models.CASCADE)
    designation = models.CharField(max_length=100)
    from_date = models.DateField()
    to_date = models.DateField()
    company = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = 'Experiences'
