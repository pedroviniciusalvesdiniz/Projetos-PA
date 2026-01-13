from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv
import os
import time
from captura_uf import capturar_uf
from verificar_cna import verificar_cna  # agora recebe driver como parâmetro
from datetime import date

load_dotenv()

def criar_driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless=new")      # ATIVADO: muito mais rápido
    chrome_options.add_argument("--incognito") # Abre em modo incognito
    # Removidas: incognito, maximized, detach (não precisa mais)

    service = Service(ChromeDriverManager().install())

    driver = webdriver.Chrome(service=service, options=chrome_options)

    return driver

def entry_account(driver):
    try:
        print("Acessando conta do Softurbano")
        driver.get("https://processoagil.com/softurbano")

        wait = WebDriverWait(driver, 20)

        campo_usuario = wait.until(EC.presence_of_element_located((By.ID, "campoUsuarioLogin")))
        campo_usuario.send_keys(os.getenv("PA_USER"))

        time.sleep(1)
    
        campo_senha = wait.until(EC.presence_of_element_located((By.ID, "campoUsuarioSenha")))
        campo_senha.send_keys(os.getenv("PA_PASSWORD"))
        
        time.sleep(1)

        wait.until(EC.element_to_be_clickable((By.ID, "kt_login_signin_submit"))).click()

        time.sleep(2)

        print("Entrou no Softurbano")

    except Exception as e:
        print(f"Erro ao entrar no Softurbano: {e}")

def take_info_lead(url):
    driver = criar_driver()  # único driver
    
    try:
        entry_account(driver)
        
        print("Acessando perfil do lead")
        driver.get(url)
        
        wait = WebDriverWait(driver, 10)
        
        nome = wait.until(EC.visibility_of_element_located((By.ID, "ctl00_ContentPlaceHolder1_DadosUsuario_CadastroAbaLinkNomeUsuario"))).text
        cpf = wait.until(EC.visibility_of_element_located((By.ID, "ctl00_ContentPlaceHolder1_DadosUsuario_CadastroAbaSpnDocumento"))).text
        telefone = wait.until(EC.visibility_of_element_located((By.ID, "ctl00_ContentPlaceHolder1_DadosUsuario_CadastroAbaSpnTelefone"))).text.replace("+", "").replace(" ", "").replace("-", "").replace("(", "").replace(")", "")
        email = wait.until(EC.visibility_of_element_located((By.ID, "ctl00_ContentPlaceHolder1_DadosUsuario_CadastroAbaSpnEmail"))).text
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
            data
        ]

        return dados_lead

    except Exception as e:
        print(f"Erro ao pegar informações do lead: {e}")
        return None
    finally:
        driver.quit()  # único quit