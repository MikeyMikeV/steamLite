# Generated by Django 4.2.4 on 2023-10-25 14:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_profile_ignore'),
        ('games', '0015_rename_game_gamemedia_game_info'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('value', models.IntegerField(choices=[(0, 0), (1, 1)])),
                ('time_stamp', models.DateField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.profile')),
            ],
        ),
        migrations.AddField(
            model_name='gamemaininfo',
            name='reviews',
            field=models.ManyToManyField(related_name='Reviews', to='games.review'),
        ),
    ]
