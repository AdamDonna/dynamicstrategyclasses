from django.db import models
from .strategies import STRATEGY_OPTIONS

def lazy_tasks():
    return list(
        zip(sorted(STRATEGY_OPTIONS.keys()), sorted(STRATEGY_OPTIONS.keys()))
    )

# Create your models here.
class StrategyMetric(models.Model):
    is_active = models.BooleanField()
    strategy = models.CharField(max_length=255, choices=lazy_tasks())

    def get_strategy(self):
        return STRATEGY_OPTIONS[self.strategy]()

    @property
    def strategy_name(self):
        return self.get_strategy().name

    @property
    def strategy_value(self):
        return self.get_strategy().run()