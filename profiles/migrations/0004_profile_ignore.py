# Generated by Django 4.2.4 on 2023-10-25 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0015_rename_game_gamemedia_game_info'),
        ('profiles', '0003_remove_profile_background_img_alter_profile_cart_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='ignore',
            field=models.ManyToManyField(blank=True, related_name='GameIgnore', to='games.gamemaininfo'),
        ),
    ]
