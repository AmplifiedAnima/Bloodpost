# Generated by Django 4.1.1 on 2022-10-19 15:20

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('apix', '0006_alter_post_options_alter_post_name_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='commentauthors',
            field=models.ManyToManyField(blank=True, related_name='commentauthors', to=settings.AUTH_USER_MODEL),
        ),
    ]
