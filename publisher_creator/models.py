from django.db import models
from django.conf import settings

class PublisherCreator(models.Model):
    name = models.CharField(max_length=256)
    image = models.ImageField(upload_to='publisher_creator/')
    desc = models.TextField()
    followers = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, null=True)

    def __str__(self):
        return self.name
