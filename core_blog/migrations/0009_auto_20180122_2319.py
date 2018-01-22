# Generated by Django 2.0.1 on 2018-01-22 17:49

from django.db import migrations, models
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0002_auto_20150616_2121'),
        ('core_blog', '0008_auto_20180117_2025'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='post_type',
            field=models.CharField(blank=True, choices=[('article', 'article'), ('tip', 'tip')], default='article', max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='tags',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]
