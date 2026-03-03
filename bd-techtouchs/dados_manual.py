from captura_uf import capturar_uf
from verificar_cna import verificar_cna
from datetime import date
from take_info_lead import criar_driver
from take_info_lead import entry_account
from create_event import creating_event
from selenium.webdriver.support.ui import WebDriverWait
import time

def pegar_dados_manual():
    driver = criar_driver()
    # wait = WebDriverWait(driver, 20)
    # entry_account(driver, wait) 
    
    
    nome = input("Digite o nome: ")
    cpf = input("Digite o cpf: ")
    telefone = input("Digite o telefone: ")
    email = input("Digite o email: ")
    ddd = telefone[2:4]
    uf = capturar_uf(ddd)
    isLawer = verificar_cna(driver, nome, uf)  # passa o mesmo driver
    data = date.today().strftime('%d/%m/%Y')
    hiperlink = f'=HYPERLINK("https://api.whatsapp.com/send?phone={telefone}"; {telefone})'

    dados_lead = {
        "nome": nome,
        "cpf": f"'{cpf.replace('.', '').replace('-', '').replace('/', '')}",
        "hiperlink": hiperlink,
        "email": email,
        "uf": uf,
        "isLawer": isLawer,
        "data": data,
        "telefone": telefone
    }

    # time.sleep(1)
    # creating_event(driver, dados_lead)

    driver.quit()

    return dados_lead
    