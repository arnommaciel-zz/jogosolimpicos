from django.test import TestCase
from django.utils import timezone

from .models import Atleta, Competicao, Modalidade, Resultado

class JogosTestCase(TestCase):

    def setUp(self):
        Atleta.objects.create( nome_completo="Usain Bolt", idade="32")
        atleta = Atleta.objects.get(nome_completo="Usain Bolt")

        Competicao.objects.create(
            nome="Corrida",
            inicio=timezone.now(),
            fim=timezone.now(),
            unidade='s',
            tentativas=1
        )
        competicao = Competicao.objects.get(nome="Corrida")

        Modalidade.objects.create(
            nome="100m Rasos",
            competicao=competicao
        )
        modalidade = Modalidade.objects.get(nome="100m Rasos")
        
        Resultado.objects.create(
            competicao=competicao,
            atleta=atleta,
            modalidade=modalidade,
            valor = 9.58
        )

    def test_jogos(self):
        atleta = Atleta.objects.get(nome_completo="Usain Bolt")
        self.assertEqual(atleta.nome_completo, 'Usain Bolt')
        
        competicao = Competicao.objects.get(nome="Corrida")
        self.assertEqual(competicao.nome, 'Corrida')
        
        modalidade = Modalidade.objects.get(nome="100m Rasos")
        self.assertEqual(modalidade.nome, '100m Rasos')
        
        resultado = Resultado.objects.get(pk=1)
        self.assertEqual(resultado.pk, 1)