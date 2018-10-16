from rest_framework import viewsets
from django.db.models import Max, Min
from django.http import HttpResponse
from rest_framework.decorators import api_view
from .models import Atleta, Competicao, Modalidade, Resultado
from .serializers import AtletaSerializer, ModalidadeSerializer, CompeticaoSerializer, ResultadoSerializer, RankingResultadoSerializer
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
    queryset_competicao = Competicao.objects.get(pk=competicao)
    queryset_modalidade = Modalidade.objects.get(pk=modalidade)
    
    queryset_ranking = Resultado.objects.filter(
        competicao=competicao,
        modalidade=modalidade
    ).values('atleta')

    if queryset_competicao.unidade == 's':
        queryset_ranking = queryset_ranking.annotate(resultado=Min('valor')).order_by("resultado")
    else :
        queryset_ranking = queryset_ranking.annotate(resultado=Max('valor')).order_by("-resultado")
    
    competicao = CompeticaoSerializer(queryset_competicao)
    modalidade = ModalidadeSerializer(queryset_modalidade)
    ranking = RankingResultadoSerializer(queryset_ranking, many=True)
    
    retorno = '{"competicao": ' + json.dumps(competicao.data) + ','
    retorno += '"modalidade": ' + json.dumps(modalidade.data) + ','
    retorno += '"ranking": ' + json.dumps(ranking.data) + '}'

    return HttpResponse(retorno, content_type="application/json")
