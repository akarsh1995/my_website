# Generated by Django 2.2.5 on 2019-09-08 07:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_auto_20190907_0836'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='contributors',
        ),
        migrations.AddField(
            model_name='contributor',
            name='project',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='contributors', to='projects.Project'),
        ),
        migrations.AlterField(
            model_name='contributor',
            name='linkedin',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='contributor',
            name='name',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
    ]
