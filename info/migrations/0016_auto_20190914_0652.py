# Generated by Django 2.2.5 on 2019-09-14 06:52

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0015_auto_20190914_0649'),
    ]

    operations = [
        migrations.AlterField(
            model_name='achievement',
            name='document',
            field=models.FileField(blank=True, default='settings.MEDIA_ROOT/defaults/default_achievements.jpg', null=True, storage=django.core.files.storage.FileSystemStorage(location='/Users/akarshjain/Programming/Python/Projects/Django/my_website/my_website/../media'), upload_to='achievements/%Y'),
        ),
    ]
