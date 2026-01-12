from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
import os 
import time 
from captura_uf import capturar_uf
from verificar_cna import verificar_cna
from datetime import date

print("entrou take")

load_dotenv()

chrome_options = Options()
chrome_options.add_argument("--headless=new")
chrome_options.add_argument("--start-maximized") # Abre maximizado
chrome_options.add_argument("--incognito") # Abre em modo incognito
chrome_options.add_experimental_option("detach", True) # Esta linha impede que o navegador feche ao final do script

# Configuração do Navegador
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

def entry_account():
    try:
        
        driver.get("https://processoagil.com/softurbano")

        # Preenchendo campo usuário
        campo_usuario = driver.find_element(By.ID, "campoUsuarioLogin")
        campo_usuario.send_keys(os.getenv("PA_USER"))

        time.sleep(1)

        # Preenchendo campo senha
        campo_senha = driver.find_element(By.ID, "campoUsuarioSenha")
        campo_senha.send_keys(os.getenv("PA_PASSWORD"))

        time.sleep(1)

        # Botão continuar conectado
        driver.find_element(By.XPATH, '//*[@id="kt_login_signin_form"]/div[4]/div/label/span').click()

        time.sleep(1)

        # Clicando no botão de entrar
        driver.find_element(By.ID, "kt_login_signin_submit").click()

    except Exception as e:
        print(f"Erro ao entrar no Softurbano: {e}")

def take_info_lead(url):
    # Entrando na conta do Softurbano
    entry_account()

    time.sleep(1)


    try:

        # Acessando perfil do lead
        driver.get(url)

        nome = driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_DadosUsuario_CadastroAbaLinkNomeUsuario").text
        cpf = driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_DadosUsuario_CadastroAbaSpnDocumento").text
        telefone = driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_DadosUsuario_CadastroAbaSpnTelefone").text.replace("+", "").replace(" ", "").replace("-", "").replace("(", "").replace(")", "")
        email = driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_DadosUsuario_CadastroAbaSpnEmail").text
        ddd = telefone[2:4]
        uf = capturar_uf(ddd)
        isLawer = verificar_cna(nome, uf)
        data = date.today().strftime('%d/%m/%Y')

        hiperlink = f"=HYPERLINK('https://api.whatsapp.com/send?phone={telefone}', {telefone})"

        dados_lead = [
            nome,
            f"'{cpf.replace(".", "").replace("-", "")}",
            hiperlink,
            email,
            uf,
            isLawer,
            data
        ]

        driver.quit()

        return dados_lead

    except Exception as e:
        print(f"Erro ao pegar informações do lead: {e}")    
        return None