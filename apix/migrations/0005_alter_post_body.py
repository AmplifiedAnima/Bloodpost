# Generated by Django 4.1.1 on 2022-10-17 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apix', '0004_alter_post_options_post_created_post_updated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='body',
            field=models.TextField(max_length=2500, null=True, verbose_name='Content'),
        ),
    ]
