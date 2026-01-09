import requests
from dotenv import load_dotenv
import os
from db_sheets import inserir_dados

load_dotenv()

api_key = os.getenv("API_KEY")
url = "https://serpapi.com/search.json"
local = input("Qual localidade deseja buscar (Cidade/UF)? ")

def buscar_dados():
   
        start = 0

        while start < 80:
            print("Iniciando busca ... Start:", start)

            # Tentativa de busca
            try:
                params = {
                    "engine": "google_maps",
                    "q": f"Escritório de advocacia  {local}",
                    "api_key": api_key,
                    "start": start,
                }

                response = requests.get(url, params=params)
                advs = response.json().get('local_results', [])
                # print(advs)

                #Vericação se retornou algum resultado
                if advs:
                    for adv in advs:

                        #Vericação se tem telefone - Não vai inserir na planilha caso não tenha
                        if adv.get('phone'):
                            
                            uf = adv.get('address', '').split()[-3].replace(",", "").replace("-", "")
                            cidade = adv.get('address', '').split()[-5].replace(",", "").replace("-", "")
                            telefone_bruto = adv.get('phone', '').replace(" ", "").replace("-", "").replace("+", "")
                            hiperlink_telefone = f'=HYPERLINK("https://wa.me/{telefone_bruto}"; "{telefone_bruto}")'

                            dados_adv = [
                                adv.get('title', ''),
                                uf,
                                cidade,
                                adv.get('address', ''),
                                hiperlink_telefone,
                                adv.get('website', ''),
                            ]

                            # Tentativa de inserir dados na planilha
                            try:
                                inserir_dados(dados_adv)
                                # print("Dados inseridos com sucesso:")
                            except Exception as e:
                                print(f"Erro ao inserir dados: {e}")
                                break
                        else:
                            print("Não há telefone")
                else:
                    print("Nenhum resultado encontrado")
                    break

            except Exception as e:
                print(f"Erro ao buscar dados: {e}")

            print("Busca finalizada", start)
            start += 20 


if __name__ == "__main__":
    buscar_dados()