from django.db import models
from datetime import datetime
from django.utils import timezone
from django.core.exceptions import ValidationError

class Modalidade(models.Model):
	
	nome = models.CharField(max_length=255, unique=True)
	competicao = models.ForeignKey(
        'Competicao', 
        on_delete=models.CASCADE,
        verbose_name="Competição"
    )
	def __str__(self):
		return self.nome

class Atleta(models.Model):
    
    nome_completo = models.CharField(max_length=255)
    idade = models.IntegerField()

    def __str__(self):
        return self.nome_completo


class Competicao(models.Model):
    
    UNIDADES = (
        ('s', 'Segundos'),
        ('m', 'Metros')
    )
    
    nome = models.CharField(max_length=150)
    inicio = models.DateTimeField()
    fim = models.DateTimeField()
    unidade = models.CharField(max_length=1, choices=UNIDADES)
    tentativas = models.IntegerField()
    
    def __str__(self):
        return self.nome
        
    class Meta:
        verbose_name_plural = "Competições"
        
    def clean(self):
        if self.inicio>self.fim:
            raise ValidationError('Informe uma data inicial menor que a data fim')

class Resultado(models.Model):
	
    competicao = models.ForeignKey(
        'Competicao', 
        on_delete=models.CASCADE,
        verbose_name="Competição"
    )
    modalidade = models.ForeignKey('Modalidade', on_delete=models.CASCADE)
    atleta = models.ForeignKey('Atleta', on_delete=models.CASCADE)
    valor = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return "Resultado"
    
    def clean(self):
        if self.competicao.inicio > timezone.now():
            raise ValidationError('Essa competição será iniciada em: ' + self.competicao.inicio.strftime('%d/%m/%Y às %H:%M') + '. Aguarde!')
        
        if self.competicao.fim < timezone.now():
            raise ValidationError('Competição encerrada em: ' + self.competicao.fim.strftime('%d/%m/%Y às %H:%M'))
        
        if Resultado.objects.filter(
            competicao=self.competicao, 
            modalidade=self.modalidade,
            atleta=self.atleta
            ).count() > self.competicao.tentativas:
            raise ValidationError('Este atleta excedeu o número de tentativas permitidas')
        
        if Modalidade.objects.filter(pk=self.modalidade.id)[0].competicao != self.competicao:
            raise ValidationError('Esta modalidade não pertence ao tipo de competição escolhida')