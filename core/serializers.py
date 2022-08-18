from rest_framework.serializers import ModelSerializer

from core.models import Categoria, Editora


class GeneroSerializer(ModelSerializer):
    class Meta:
        model = Genero
        fields = "__all__"

class GravadoraSerializer(ModelSerializer):
    class Meta:
        model = Gravadora
        fields = "__all__"
        