import requests

def capturar_uf(ddd):
    try:
        response = requests.get(f"https://brasilapi.com.br/api/ddd/v1/{ddd}")
        if response.status_code == 200:
            uf = response.json().get("state")
            return uf
        else:
            print("DDD não encontrado.")
            return None
    except Exception as e:
        print(f"Alconteceu algum erro: {e}")
        return None