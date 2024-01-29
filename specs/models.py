from django.db import models
from django.core.validators import MinValueValidator
from games.models import Game
from django.conf import settings

class SpecsMixin(models.Model):
    os = models.ForeignKey('OS', on_delete=models.PROTECT)
    processor = models.ForeignKey("Processor", on_delete = models.PROTECT)    # Удалить null = true после миграции
    graphics = models.ForeignKey('Graphics', on_delete = models.PROTECT, null = True)
    ram = models.IntegerField(null = True)
    
    class Meta:
        abstract = True

class MinimumRequirements(SpecsMixin):
    game = models.ForeignKey(Game, on_delete = models.CASCADE)
    DIRECTX_CHOICES = (
        ('DirectX 9','DirectX 9'),
        ('DirectX 10','DirectX 10'),
        ('DirectX 11','DirectX 11'),
        ('DirectX 12','DirectX 12'),   
    )
    directX = models.CharField(max_length = 50, choices=DIRECTX_CHOICES, null=True)
    storage = models.IntegerField(validators = (MinValueValidator(1,'Не возможно ввести чило меньше 1'),), null=True)

    def __str__(self):
        return f'Min. req. for {self.game.title}' 

class RecommendedRequirements(SpecsMixin):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    DIRECTX_CHOICES = (
        ('DirectX 9','DirectX 9'),
        ('DirectX 10','DirectX 10'),
        ('DirectX 11','DirectX 11'),
        ('DirectX 12','DirectX 12'),   
    )
    directX = models.CharField(max_length = 50, choices=DIRECTX_CHOICES, null=True)
    storage = models.IntegerField(validators = (MinValueValidator(1,'Не возможно ввести чило меньше 1'),), null=True)

    def __str__(self):
        return f'Rec. req. for {self.game.title}'

class UsersSpec(SpecsMixin):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)

class OS(models.Model):
    name = models.CharField(max_length = 128)
    BIT_CHOICES = (
        (32, 32),
        (64, 64),
    )
    bit = models.IntegerField(default = 2, choices = BIT_CHOICES)

    def __str__(self):
        return f'{self.name} ({self.bit}bit)'
    
class Processor(models.Model):
    BRAND_CHOICES = (
        ('Intel', 'Intel'),
        ('AMD', 'AMD'),
    )
    CORE_CHOICES = (
        ('Core', 'Core'),
        ('Dual', 'Dual-Core'),
        ('Quad_core', 'Quad_core'),
    )
    brand = models.CharField(max_length = 128, choices = BRAND_CHOICES) 
    core_type = models.CharField(max_length = 128, choices = CORE_CHOICES, null = True, blank = True)
    name = models.CharField(max_length = 128)
    model = models.CharField(max_length = 50)
    speed = models.DecimalField(
        validators=(
            MinValueValidator(1, 'Введенное значение ниже допустимого'),
        ),
        max_digits=2,
        decimal_places=1,
        help_text='GHz'
    )

    def __str__(self) -> str:
        return f'{self.brand} {self.core_type} {self.model}'

class Graphics(models.Model):
    BRAND_CHOICES = (
        ('NVIDIA', 'NVIDIA'),
        ('AMD', 'AMD'),
    )
    brand = models.CharField(max_length = 128, choices=BRAND_CHOICES, default=None)
    name = models.CharField(max_length = 128)
    model = models.CharField(max_length = 128)
    vram = models.IntegerField(validators = (MinValueValidator(1,'Не возможно ввести чило меньше 1'),))