from django.contrib import admin
from .models import Game,GameMainInfo, GamePriceInfo, GameSecondaryInfo, GameMedia, Genre,Review


admin.site.register(Game)
admin.site.register(GameMainInfo)
admin.site.register(GamePriceInfo)
admin.site.register(GameSecondaryInfo)
admin.site.register(GameMedia)
admin.site.register(Genre)
admin.site.register(Review)