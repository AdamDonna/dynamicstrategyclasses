from rest_framework import routers, serializers, viewsets
from .models import StrategyMetric

class StrategySerializer(serializers.ModelSerializer):
    class Meta:
        model = StrategyMetric
        fields = ("pk", "strategy_name", "strategy_value",)

class StrategyApi(viewsets.ModelViewSet):
    queryset = StrategyMetric.objects.all()
    serializer_class = StrategySerializer