from sheets import inserir_dados
from take_info_lead import take_info_lead
from redirect_wpp import redirect_wpp


def main():
    url = input( "Digite a url do perfil: ")
    dados_lead = take_info_lead(url)
    telefone = dados_lead[-1]
    primeiro_nome = dados_lead[0].split()[0]
    print(dados_lead)

    if dados_lead != None:
        inserir_dados(dados_lead)
        redirect_wpp(primeiro_nome, telefone)
    

if __name__ == "__main__":
    main()
