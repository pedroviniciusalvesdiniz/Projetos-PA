from sheets import inserir_dados
from take_info_lead import take_info_lead


def main():
    url = input( "Digite a url do perfil: ")
    dados_lead = take_info_lead(url)

    if dados_lead != None:
        inserir_dados(dados_lead)
    

if __name__ == "__main__":
    main()
