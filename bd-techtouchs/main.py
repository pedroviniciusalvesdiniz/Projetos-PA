from sheets import inserir_dados
from take_info_lead import take_info_lead
from redirect_wpp import redirect_wpp
from dados_manual import pegar_dados_manual


def main():
    while True:
        opcao = input("Digite 1 para inserir manualmente; qualquer outra tecla para captar pelo perfil: ")
        if opcao == '1':
            dados_lead = pegar_dados_manual()
        else:
            url = input( "Digite a url do perfil: ")
            dados_lead = take_info_lead(url)

        telefone = dados_lead[-1]
        primeiro_nome = dados_lead[0].split()[0]
        print(dados_lead)

        if dados_lead != None:
            inserir_dados(dados_lead)
            redirect_wpp(primeiro_nome, telefone)

            continuar = input("Deseja continuar? (1 para sim, outra tecla para não): ")
            if continuar != '1':
                break
    
    

if __name__ == "__main__":
    main()
