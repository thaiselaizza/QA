import requests
import logging

LOGGER = logging.getLogger(__name__)
id_criado = None
id_produto_criado = None

def test_criar_usuario():
    global id_criado
    headers = {
        'Accept': '*/*',
        'User-Agent': 'request'
    }

    url = "https://serverest.dev/usuarios"
    novo_usuario = {'nome':'Thais Colares','email':'thaiserc@gmail.com','password': '654321','administrador':'true'}
    resposta = requests.post(url,headers=headers,data=novo_usuario)
    resposta_dicionario = resposta.json()
    LOGGER.info(resposta_dicionario)

    if resposta.status_code == 201:
        mensagem = resposta_dicionario['message']
        id = resposta_dicionario['_id']
        assert id is not None and mensagem == "Cadastro realizado com sucesso"
        id_criado = id

    if resposta.status_code == 400:
        mensagem = resposta_dicionario['message']
        assert mensagem == "Este email já está sendo usado"

def test_consulta_usuario_criado():
    global id_criado
    LOGGER.info(id_criado)

    headers = {
        'Accept': '*/*',
        'User-Agent': 'request'
    }

    url = "https://serverest.dev/usuarios/"

    resposta = requests.get(url + str(id_criado), headers=headers)
    resposta_dicionario = resposta.json()
    LOGGER.info(resposta_dicionario)
    if resposta.status_code == 200:
        usuario_id = resposta_dicionario['_id']

        assert usuario_id == id_criado

    if resposta.status_code == 400:
        mensagem = resposta_dicionario['message']
        assert mensagem == "Usuário não encontrado"

    id_criado = None

def realiza_login():
    headers = {
        'Accept': '*/*',
        'User-Agent': 'request',

    }

    url = "https://serverest.dev/login"
    login = {'email': 'thaiserc@gmail.com', 'password': '654321'}
    resposta = requests.post(url, headers=headers, data=login)
    resposta_dicionario = resposta.json()
    LOGGER.info(resposta_dicionario)

    if resposta.status_code == 200:
        mensagem = resposta_dicionario['message']
        token = resposta_dicionario['authorization']
        assert token is not None and mensagem == "Login realizado com sucesso"
        return token

    if resposta.status_code == 400:
        mensagem = resposta_dicionario['message']
        assert mensagem == "Email e/ou senha inválidos"




def test_criar_produto():

    global id_produto_criado
    headers = {
        'Accept': '*/*',
        'User-Agent': 'request',
        'Authorization': realiza_login()
    }

    url = "https://serverest.dev/produtos"
    novo_produto = {'nome': 'Livro Harry Potter e o Enigma do Príncipe', 'preco': '239', 'descricao': 'Livro Harry Potter e o Enigma do Príncipe capa dura', 'quantidade': '3'}
    resposta = requests.post(url, headers=headers, data=novo_produto)
    resposta_dicionario = resposta.json()
    LOGGER.info(resposta_dicionario)



    if resposta.status_code == 201:
        mensagem = resposta_dicionario['message']
        id = resposta_dicionario['_id']
        assert id is not None and mensagem == "Cadastro realizado com sucesso"
        id_produto_criado = id

    if resposta.status_code == 400:
        mensagem = resposta_dicionario['message']
        assert mensagem == "Já existe produto com esse nome"

    if resposta.status_code == 401:
        mensagem = resposta_dicionario['message']
        assert mensagem == "Token de acesso ausente, inválido, expirado ou usuário do token não existe mais"

    if resposta.status_code == 403:
        mensagem = resposta_dicionario['message']
        assert mensagem == "Rota exclusiva para administradores"


def test_consulta_produto_criado():
    global id_produto_criado
    LOGGER.info(id_produto_criado)

    headers = {
        'Accept': '*/*',
        'User-Agent': 'request'
    }

    url = "https://serverest.dev/produtos/"

    resposta = requests.get(url + str(id_produto_criado), headers=headers)
    resposta_dicionario = resposta.json()
    LOGGER.info(resposta_dicionario)
    if resposta.status_code == 200:
        produto_id = resposta_dicionario['_id']

        assert produto_id == id_produto_criado

    if resposta.status_code == 400:
        mensagem = resposta_dicionario['message']
        assert mensagem == "Produto não encontrado"

    id_produto_criado = None




