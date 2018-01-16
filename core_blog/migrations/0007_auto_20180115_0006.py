# Generated by Django 2.0.1 on 2018-01-14 18:36

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core_blog', '0006_auto_20180113_1752'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='publish',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='draft',
            field=models.BooleanField(default=True),
        ),
    ]