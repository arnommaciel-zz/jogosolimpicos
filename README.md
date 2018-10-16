# Jogos olimpicos
### Teste prático da EstanteVirtual

Criar uma API REST em Python/Django para o COB (Comitê Olímico Brasileiro), que será responsável por marcar e dizer os vencedores das modalidades:

* 100m rasos: Menor tempo vence
* Lançamento de Dardo: Maior distância vence

### Criado e Testado com:
* virtualenv 16.0.0
* Python 3.7.0
* pip 18.1
* django 2.1.2

### Executando a API:
1. Baixe o projeto no local desejado.
```
git clone https://github.com/arnommaciel/jogosolimpicos.git
```
2. Abra a pasta do projeto pelo terminal: 
```
cd jogosolimpicos
```
3. Instale o virtualenv no projeto: 
```
virtualenv env
```
4. Ative o virtualenv:
```
source env/bin/activate
```
5. Execute os comandos abaixo para iniciar o projeto:
``` 
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py makemigrations jogos
python manage.py migrate
python manage.py runserver
```
6. Acesse o admin pela url: http://127.0.0.1:8000/admin/

# Testando a aplicação
Execute o camando abaixo:
```
python manage.py test
``` 
# Cadastrando os dados
1. Cadastre uma competição 
```
exemplo: Corrida
``` 
2. Cadastre a modalidade da competição
```
exemplo: 100m Rasos
``` 
3. Cadastre os atletas

4. Cadastre os resultados

### URLs da API
* API Root - http://127.0.0.1:8000/api/v1/jogos/
* Atletas - http://127.0.0.1:8000/api/v1/jogos/atletas/
* Competições - http://127.0.0.1:8000/api/v1/jogos/competicoes/
* Modalidades - http://127.0.0.1:8000/api/v1/jogos/modalidades/
* Resultados - http://127.0.0.1:8000/api/v1/jogos/resultados/
* Ranking - http://127.0.0.1:8000/api/v1/jogos/competicao/1/modalidade/1/ranking