# Generated by Django 2.1.7 on 2019-04-08 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0010_videos_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videos',
            name='slug',
            field=models.SlugField(editable=False, max_length=3, null=True, unique=True),
        ),
    ]
