from captura_uf import capturar_uf
from verificar_cna import verificar_cna
from datetime import date
from take_info_lead import criar_driver

def pegar_dados_manual():
    driver = criar_driver()
    nome = input("Digite o nome: ")
    cpf = input("Digite o cpf: ")
    telefone = input("Digite o telefone: ")
    email = input("Digite o email: ")
    ddd = telefone[2:4]
    uf = capturar_uf(ddd)
    isLawer = verificar_cna(driver, nome, uf)  # passa o mesmo driver
    data = date.today().strftime('%d/%m/%Y')
    hiperlink = f'=HYPERLINK("https://api.whatsapp.com/send?phone={telefone}"; {telefone})'

    dados_lead = [
        nome,
        f"'{cpf.replace('.', '').replace('-', '')}",
        hiperlink,
        email,
        uf,
        isLawer,
        data,
        telefone
    ]
    return dados_lead
    