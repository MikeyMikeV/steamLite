# Generated by Django 4.2.4 on 2023-09-13 13:47

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('publisher_creator', '0001_initial'),
        ('games', '0010_game_creator_game_publisher'),
    ]

    operations = [
        migrations.CreateModel(
            name='GameSecondaryInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_singleplayer', models.BooleanField(default=False, verbose_name='Одиночная игра')),
                ('is_multiplayer', models.BooleanField(default=False, verbose_name='Мультиплэер')),
                ('has_crossplatforer', models.BooleanField(default=False, verbose_name='Кросплатформенная')),
            ],
        ),
        migrations.RemoveField(
            model_name='game',
            name='age_rist',
        ),
        migrations.RemoveField(
            model_name='game',
            name='creator',
        ),
        migrations.RemoveField(
            model_name='game',
            name='desc',
        ),
        migrations.RemoveField(
            model_name='game',
            name='discount_percent',
        ),
        migrations.RemoveField(
            model_name='game',
            name='early_access',
        ),
        migrations.RemoveField(
            model_name='game',
            name='genre',
        ),
        migrations.RemoveField(
            model_name='game',
            name='has_crossplatforer',
        ),
        migrations.RemoveField(
            model_name='game',
            name='has_discount',
        ),
        migrations.RemoveField(
            model_name='game',
            name='is_multiplayer',
        ),
        migrations.RemoveField(
            model_name='game',
            name='is_singleplayer',
        ),
        migrations.RemoveField(
            model_name='game',
            name='min_sys_req',
        ),
        migrations.RemoveField(
            model_name='game',
            name='poster',
        ),
        migrations.RemoveField(
            model_name='game',
            name='price',
        ),
        migrations.RemoveField(
            model_name='game',
            name='publish_date',
        ),
        migrations.RemoveField(
            model_name='game',
            name='publisher',
        ),
        migrations.RemoveField(
            model_name='game',
            name='rec_sys_req',
        ),
        migrations.AlterField(
            model_name='game',
            name='is_dlc',
            field=models.BooleanField(default=False, help_text='Поставьте галочку если это Доп. Контент к игре', verbose_name='Дополнительный контент'),
        ),
        migrations.AlterField(
            model_name='game',
            name='main_game',
            field=models.ForeignKey(blank=True, help_text='Выбрать игру из списка которой пренадлежит Доп. Контент', null=True, on_delete=django.db.models.deletion.PROTECT, to='games.game'),
        ),
        migrations.CreateModel(
            name='GamePriceInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField(validators=[django.core.validators.MinValueValidator(0, 'Введено значение ниже допустимого')], verbose_name='Цена')),
                ('has_discount', models.BooleanField(default=False, verbose_name='Есть скидка')),
                ('discount_percent', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)], verbose_name='Скидка')),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='games.game')),
            ],
        ),
        migrations.CreateModel(
            name='GameMainInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('poster', models.ImageField(upload_to='games/game_posters')),
                ('game_background', models.ImageField(upload_to='games/game_background')),
                ('description', models.TextField(verbose_name='Описание')),
                ('early_access', models.DateField(blank=True, null=True, verbose_name='Ранний доступ')),
                ('publish_date', models.DateField(verbose_name='Дата релиза')),
                ('age_rist', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)], verbose_name='Возраст. органичение')),
                ('creator', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='creator', to='publisher_creator.publishercreator')),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='games.game')),
                ('genre', models.ManyToManyField(to='games.genre')),
                ('publisher', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='publisher', to='publisher_creator.publishercreator')),
            ],
        ),
        migrations.AlterField(
            model_name='gamemedia',
            name='game',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='games.gamemaininfo'),
        ),
    ]
