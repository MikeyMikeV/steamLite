# Generated by Django 4.2.4 on 2023-09-13 14:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0011_gamesecondaryinfo_remove_game_age_rist_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='gamemaininfo',
            name='price_info',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, to='games.gamepriceinfo'),
            preserve_default=False,
        ),
    ]
