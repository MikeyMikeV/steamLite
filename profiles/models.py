from django.db import models
from games.models import GameMainInfo
from django.utils import timezone
from django.conf import settings

class Profile(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete= models.CASCADE)
    avatar = models.ImageField(default= 'profiles/avatars/default.jpeg',upload_to='profiles/avatars/')
    profile_name = models.CharField(max_length=50)
    date_of_birth = models.DateField(null=True)
    country = models.CharField(max_length=128,null=True)
    district = models.CharField(max_length=128,null=True)
    city = models.CharField(max_length=128,null=True)
    # BACKGROUND_CHOICES = (
    #     (1, 'images/backgrounds/default.webp'),
    # )
    # background_img = models.CharField(default=1, max_length=256, choices=BACKGROUND_CHOICES)
    date_joined = models.DateTimeField(auto_now_add=timezone.now)
    last_active = models.DateTimeField(auto_now=timezone.now)
    profile_level = models.IntegerField(default=0)
    xp_level = models.IntegerField(default=0)
    # [
    #     (0, 0),
    #     (1, 100),
    #     (2, 350),
    #     (3, 800),
    #     (4, 1300),
    #     (5, 1800),
    #     (6, 2500)
    # ]
    summary = models.CharField(max_length=256,null=True,blank=True)
    # cart = None
    friend_list = models.ManyToManyField('self', symmetrical=False, blank=True)
    # fav_game = None
    game_list = models.ManyToManyField(GameMainInfo, related_name='GameList', blank=True)
    cart = models.ManyToManyField(GameMainInfo, related_name='Cart', blank=True)
    wishlist = models.ManyToManyField(GameMainInfo, related_name='Wishlist', blank=True)
    ignore = models.ManyToManyField(GameMainInfo,related_name='GameIgnore',blank=True)

    def __str__(self):
        return f'{self.user.username}\'s {self.profile_name} profile'
    
from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_profile(sender, instance, created, **kwargs):
    if created:
        profile_name = instance.username
        Profile.objects.create(user = instance, profile_name = profile_name)
