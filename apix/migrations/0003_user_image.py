# Generated by Django 4.1.1 on 2022-10-15 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apix', '0002_alter_post_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/profile/'),
        ),
    ]
