# Generated by Django 2.2.5 on 2019-09-09 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_article_short_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='short_description',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]
