# Generated by Django 2.0.1 on 2018-01-17 14:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core_blog', '0007_auto_20180115_0006'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-publish']},
        ),
    ]