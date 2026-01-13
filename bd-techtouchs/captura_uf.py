import requests

def capturar_uf(ddd):
    try:
        print("Capturando DDD baseado no número.")
        response = requests.get(f"https://brasilapi.com.br/api/ddd/v1/{ddd}")
        if response.status_code == 200:
            uf = response.json().get("state")
            print("UF lead: ", uf)
            return uf
        else:
            print("DDD não encontrado.")
            return None
    except Exception as e:
        print(f"Alconteceu algum erro: {e}")
        return None

if __name__ == "__main__":
    ddd = input("Digite o DDD: ")
    uf = capturar_uf(ddd)
    if uf:
        print(f"DDD {ddd} corresponde a {uf}")