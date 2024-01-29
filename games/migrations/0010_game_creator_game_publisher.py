# Generated by Django 4.2.4 on 2023-09-11 15:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('publisher_creator', '0001_initial'),
        ('games', '0009_alter_genre_poster'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='creator',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='creator', to='publisher_creator.publishercreator'),
        ),
        migrations.AddField(
            model_name='game',
            name='publisher',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='publisher', to='publisher_creator.publishercreator'),
        ),
    ]
