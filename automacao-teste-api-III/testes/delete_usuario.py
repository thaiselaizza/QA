import requests

def test_delete_usuario():
    headers = {
        'Accept': '*/*',
        'User-Agent': 'request'
    }

    id = "hCBpifPhmEQAzSGY"

    url = "https://serverest.dev/usuarios/"

    resposta = requests.delete(url + str(id), headers=headers)
    resposta_dicionario = resposta.json()

    assert resposta.status_code == 200
