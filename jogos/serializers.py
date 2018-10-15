from rest_framework import serializers
from .models import Atleta, Competicao, Modalidade, Resultado

class AtletaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Atleta
        fields = ('__all__')

class CompeticaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Competicao
        fields = ('__all__')

class ModalidadeSerializer(serializers.ModelSerializer):
    competicao = CompeticaoSerializer(read_only=True)
    class Meta:
        model = Modalidade
        fields = ('__all__')

class ResultadoSerializer(serializers.ModelSerializer):
    competicao = CompeticaoSerializer(read_only=True)
    modalidade = ModalidadeSerializer(read_only=True)
    atleta = AtletaSerializer(read_only=True)
    valor = serializers.DecimalField(max_digits=6, decimal_places=2)

    class Meta:
        model = Resultado
        fields = ('__all__')

class RankingModalidadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Modalidade
        exclude = ('competicao',)

class RankingResultadoSerializer(serializers.Serializer):
    
    def get_atleta(self, obj):
        return AtletaSerializer(Atleta.objects.get(pk=obj['atleta'])).data        

    atleta = serializers.SerializerMethodField()
    resultado = serializers.DecimalField(max_digits=6, decimal_places=2)