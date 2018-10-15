from django.contrib import admin
from django.conf.urls import url, include
from django.urls import path
from rest_framework import routers

from jogos import views

router = routers.DefaultRouter()
router.register(r'atletas', views.AtletaViewSet)
router.register(r'competicoes', views.CompeticaoViewSet)
router.register(r'modalidades', views.ModalidadeViewSet)
router.register(r'resultados', views.ResultadoViewSet)

urlpatterns = [
	url(r'^', include(router.urls)),
	#url(r'^competicao/<int:competicao>', views.ranking),
	path('competicao/<int:competicao>/modalidade/<int:modalidade>/ranking', views.ranking),
]