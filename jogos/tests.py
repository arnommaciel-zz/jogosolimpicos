from django.test import TestCase, RequestFactory
from django.utils import timezone
from datetime import datetime, timedelta

from .models import Atleta, Competicao, Modalidade, Resultado

class JogosModelTests(TestCase):

    def setUp(self):
        print ("Inicio cadastro")
        self.factory = RequestFactory()
        Atleta.objects.create(
            nome_completo="Joao da Silva",
            idade="20"
        )
        Competicao.objects.create(
            nome="Corrida",
            inicio=timezone.now(),
            fim=timezone.now(),
            unidade='s',
            tentativas=1
        )
        Modalidade.objects.create(
            nome="100m Rasos",
            competicao=1
        )
        print ("Fim cadastro")

    def leitura_atleta(self):
        print ("Inicio teste leitura atleta")
        atleta = Atleta.objects.get(nome="Joao")

        print("Atleta")
        self.assertEqual(atleta.nome, 'Joao')
        print ("Fim teste leitura atleta")

    def leitura_competicao(self):
        print ("Inicio teste leitura competicoes")
        competicao = Competicao.objects.get(nome="Corrida")
        
        print("Competicao")
        self.assertEqual(competicao.nome, 'Corrida')
        print ("Fim teste leitura competicoes")

    def leitura_modalidade(self):
        print ("Inicio teste leitura modalidade")
        modalidade = Modalidade.objects.get(nome="100m Rasos")
        
        print("Competicao")
        self.assertEqual(modalidade.nome, '100m Rasos')
        print ("Fim teste leitura modalidade")


    def cadastro_resultado(self):
        print ("Inicio cadastro resultado")
        atleta = Atleta.objects.get(nome="Joao")
        competicao = Competicao.objects.get(nome="Corrida")
        modalidade = Modalidade.objects.get(nome="100m Rasos")
        
        Resultado.objects.create(
            competicao=competicao,
            atleta=atleta,
            modalidade=modalidade,
            valor = 20.33
        )

        resultado = Resultado.objects.get(pk=1)
        print("Resultado")
        self.assertEqual(resultado.pk, 1)
        print ("Fim cadastro resultado")

