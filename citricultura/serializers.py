from rest_framework import serializers
from .models import Lote


class LoteSerializer(serializers.ModelSerializer):
    total = serializers.ReadOnlyField()

    class Meta:
        model = Lote
        fields = ["id", "produtor", "variedade", "caixas", "preco_caixa", "data", "total"]