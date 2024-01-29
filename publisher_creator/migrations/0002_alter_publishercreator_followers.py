# Generated by Django 4.2.4 on 2023-09-13 14:34

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('publisher_creator', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publishercreator',
            name='followers',
            field=models.ManyToManyField(blank=True, null=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
