from django.db import models
from django.dispatch import receiver
import os
from django.core.validators import MinValueValidator, MaxValueValidator
from publisher_creator.models import PublisherCreator

from hitcount.models import HitCountMixin, HitCount
from django.contrib.contenttypes.fields import GenericRelation

class Game(models.Model):
    title = models.CharField(max_length=256, verbose_name='Название', unique=True)
    game_icon = models.ImageField(upload_to='game_icons')
    is_dlc = models.BooleanField(
        default=False,
        verbose_name='Дополнительный контент', 
        help_text='Поставьте галочку если это Доп. Контент к игре'
    )
    main_game = models.ForeignKey(
        'Game', 
        on_delete=models.PROTECT,
        null=True,
        blank=True, 
        help_text='Выбрать игру из списка которой пренадлежит Доп. Контент'
    )
    size = models.FloatField(
        validators=(
            MinValueValidator(0),
        ),
        verbose_name='Размер игры'
    )
    # game_file

    def __str__(self):
        return self.title
    
class GamePriceInfo(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    price = models.IntegerField(
        validators=(
            MinValueValidator(0,'Введено значение ниже допустимого'),
        ),
        verbose_name='Цена',
    )
    has_discount = models.BooleanField(default = False, verbose_name = 'Есть скидка')
    discount_percent = models.IntegerField(
        validators=(
            MinValueValidator(1),
            MaxValueValidator(100),
        ),
        verbose_name='Скидка'
    )

    def __str__(self) -> str:
        if self.has_discount:
            return f'{self.game.title} {self.price}т ({self.discount_percent}%)'
        return f'{self.game.title} {self.price}т'
    
    def get_discount_price(self):
        if self.has_discount:
            return self.price-self.price*self.discount_percent/100
        return self.price

class GameMainInfo(models.Model, HitCountMixin):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    poster = models.ImageField(upload_to='games/game_posters')
    game_background = models.ImageField(upload_to='games/game_background')
    description = models.TextField(verbose_name='Описание')
    publisher = models.ForeignKey(PublisherCreator, on_delete=models.PROTECT, related_name='publisher', null=True)
    early_access = models.DateField(verbose_name='Ранний доступ', null=True, blank=True)
    publish_date = models.DateField(verbose_name='Дата релиза')
    genre = models.ManyToManyField('Genre')
    creator = models.ForeignKey(PublisherCreator, on_delete=models.PROTECT, related_name='creator', null=True)
    age_rist = models.IntegerField(
        validators=(
            MinValueValidator(0),
        ),
        verbose_name='Возраст. органичение'
    )
    price_info = models.ForeignKey(GamePriceInfo, on_delete=models.PROTECT, null=True, blank=True)
    hit_count_generic = GenericRelation(
        HitCount, 
        object_id_field='object_pk',
        related_query_name='hit_count_generic_relation'
    )
    reviews = models.ManyToManyField("Review", related_name='Reviews', blank=True)

    def get_current_hit_count(self):
        return self.hit_count.hits    

    def __str__(self):
        return f'Desc. for {self.game.title}'
    
class GameSecondaryInfo(models.Model):
    game = models.ForeignKey(Game, on_delete= models.CASCADE, null=True)
    is_singleplayer = models.BooleanField(default = False, verbose_name = 'Одиночная игра')
    is_multiplayer = models.BooleanField(default = False, verbose_name = 'Мультиплэер')
    has_crossplatforer = models.BooleanField(default = False, verbose_name = 'Кросплатформенная') 
    #TODO - доделать Все условные поля
    # languages = models.ManyToManyField(Language)
    # platforms = models.ManyToManyField(Platform)

class GameMedia(models.Model):
    file = models.FileField(upload_to='game_media')
    game_info = models.ForeignKey(GameMainInfo, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.game_info.game.title}: {self.file}'
    
class Genre(models.Model):
    name = models.CharField(max_length=100)
    poster = models.ImageField(upload_to='genre/', null=True, blank=True)

    def __str__(self):
        return self.name
    

from profiles.models import Profile
class Review(models.Model):
    # game_info
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    text = models.TextField()
    VALUE_CHOICES = (
        (0,0),
        (1,1),
    )
    value = models.IntegerField(choices=VALUE_CHOICES)
    time_stamp = models.DateField(auto_now_add=True)

@receiver(models.signals.post_delete, sender = GameMedia)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    if instance.file and os.path.isfile(instance.file.path):
        print(f'File \'{instance.file}\' is deleted')
        os.remove(instance.file.path)

@receiver(models.signals.post_delete, sender = Game)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    if instance.game_icon and os.path.isfile(instance.game_icon.path):
        print(f'File \'{instance.game_icon}\' is deleted')
        os.remove(instance.game_icon.path)

# @receiver(models.signals.pre_save, sender = Game)
# def auto_resolve_file_on_change(sender, instance, **kwargs):
#     if not instance.pk:
#         return False
    
#     try:
#         game = Game.objects.get(pk = instance.pk)
#         old_poster = game.poster
#         old_icon = game.game_icon
#     except Game.DoesNotExist:
#         return False
    
#     new_poster = instance.poster
#     new_icon = instance.game_icon

#     if not old_poster==new_poster:
#         if os.path.isfile(old_poster.path):
#             os.remove(old_poster.path)

#     if not old_icon==new_icon:
#         if os.path.isfile(old_icon.path):
#             os.remove(old_icon.path)