# Generated by Django 2.2.5 on 2019-09-07 08:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Contributor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('linkedin', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=150)),
                ('start_date', models.DateField(blank=True)),
                ('end_date', models.DateField(blank=True, help_text='If currently working leave as it is')),
                ('url', models.URLField()),
                ('description', models.TextField(blank=True)),
                ('currently_working', models.BooleanField()),
                ('slug', models.CharField(blank=True, max_length=100)),
                ('display_image', models.ImageField(blank=True, upload_to='')),
                ('contributors', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to='projects.Contributor')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='projects', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Projects',
            },
        ),
    ]
