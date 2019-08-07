from .models import Demanda
from rest_framework import serializers
from user.serializer import UserSerializer


class DemandaCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Demanda
        fields = ("id", "descricao")
        extra_kwargs = {"anunciante_id": {"write-only": True}}


class DemandaSerializer(serializers.ModelSerializer):
    anunciante = UserSerializer()

    class Meta:
        model = Demanda
        fields = ("id", "descricao", "endereco", "contato", "anunciante", "finalizado")
        depth = 1
