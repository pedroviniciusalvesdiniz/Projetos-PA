from datetime import date
from captura_uf import capturar_uf
from verificar_cna import verificar_cna
from sheets import inserir_dados
from send_wpp import send_wpp

nome = input("Digite o nome: ")
cpf = input("Digite o cpf: ").replace(".", "").replace("-", "")
telefone = input("Digite o telefone: ").replace("+", "").replace(" ", "").replace("-", "")
ddd = telefone[2:4]
email = input("Digite o email: ")
uf = capturar_uf(ddd)
data = date.today().strftime('%d/%m/%Y')
lawyer = verificar_cna(nome, uf)

def main():
    hiperlink_wpp = f'=HYPERLINK("https://api.whatsapp.com/send?phone={telefone}"; "{telefone}")'

    dados_lead = [nome, cpf, hiperlink_wpp, email, uf, lawyer, data]
    inserir_dados(dados_lead)
    send_wpp(telefone, nome)

if __name__ == "__main__":
    main()
