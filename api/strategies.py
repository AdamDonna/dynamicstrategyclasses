STRATEGY_OPTIONS = {}

def register(cls):
    STRATEGY_OPTIONS[cls.get_name(cls)] = cls
    return cls

class Strategy:
    name = None

    def get_name(self):
        if not self.name:
            raise NotImplementedError
        return self.name

    def run(self, *args, **kwargs):
        raise NotImplementedError

@register
class CountStrategy(Strategy):
    name = "Count Strategy"

    def run(self, *args, **kwargs):
        return 100


@register
class BoolStrategy(Strategy):
    name = "Bool Strategy"

    def run(self, *args, **kwargs):
        return False
