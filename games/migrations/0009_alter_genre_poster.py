# Generated by Django 4.2.4 on 2023-09-11 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0008_alter_genre_poster'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genre',
            name='poster',
            field=models.ImageField(blank=True, null=True, upload_to='genre/'),
        ),
    ]
