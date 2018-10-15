from rest_framework import viewsets
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from .models import Atleta, Competicao, Modalidade, Resultado
from .serializers import AtletaSerializer, ModalidadeSerializer, CompeticaoSerializer, ResultadoSerializer, RankingResultadoSerializer, RankingModalidadeSerializer
import json

class AtletaViewSet(viewsets.ModelViewSet):
    queryset = Atleta.objects.all().order_by("nome_completo")
    serializer_class = AtletaSerializer

class ModalidadeViewSet(viewsets.ModelViewSet):
    queryset = Modalidade.objects.all().order_by("nome")
    serializer_class = ModalidadeSerializer


class CompeticaoViewSet(viewsets.ModelViewSet):
    queryset = Competicao.objects.all().order_by("nome")
    serializer_class = CompeticaoSerializer

class ResultadoViewSet(viewsets.ModelViewSet):
    queryset = Resultado.objects.all()
    serializer_class = ResultadoSerializer


@api_view(['GET'])
def ranking(request, competicao, modalidade):
    comp = Competicao.objects.get(pk=competicao)
    comp = CompeticaoSerializer(comp)

    mod = Modalidade.objects.get(pk=modalidade)
    mod = RankingModalidadeSerializer(mod)
    
    ranking = Resultado.objects.filter(
        competicao=competicao,
        modalidade=modalidade
    ).order_by('valor')
    ranking = RankingResultadoSerializer(ranking, many=True)
    
    result = '{ "competicao": ' + json.dumps(comp.data) + ','
    result += '"modalidade": ' + json.dumps(mod.data) + ','
    result += '"ranking": ' + json.dumps(ranking.data) + '}'

    return HttpResponse(result, content_type="application/json")
