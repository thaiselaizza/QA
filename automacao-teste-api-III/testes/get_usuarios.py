import requests

headers = {
    'Accept': '*/*',
    'User-Agent': 'request',
}

url = "https://serverest.dev/usuarios"

resposta = requests.get(url, headers=headers)
print(resposta.text)