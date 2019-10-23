from django.contrib import admin
from . import models

class StrategyAdmin(admin.ModelAdmin):
    pass

admin.site.register(models.StrategyMetric, StrategyAdmin)