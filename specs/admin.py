from django.contrib import admin
from .models import MinimumRequirements, RecommendedRequirements, OS, Processor, Graphics
# Register your models here.

admin.site.register(MinimumRequirements)
admin.site.register(RecommendedRequirements)
admin.site.register(OS)
admin.site.register(Processor)
admin.site.register(Graphics)
