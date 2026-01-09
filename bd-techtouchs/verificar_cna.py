from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Configurações de Opções do Chrome
chrome_options = Options()
chrome_options.add_argument("--headless=new") # Não abrir a janela do navegador

# Configuração do Navegador
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

def verificar_cna(nome, uf):
    try:
        # Abrindo a página do CNA no navegador
        driver.get("https://cna.oab.org.br/")

        # Localizando o campo de nome e preenchendo
        campo_nome = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "txtName"))
        )
        campo_nome.send_keys(f'"{nome}"')

        # Localizando e clicando no botão de buscar
        botao_buscar = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "btnFind"))
        )
        botao_buscar.click()

        # Verificando se o nome completo do lead consta na CNA
        try:
            resultados = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.ID, "divResult"))
            )

            # Verificando cada resultado obtido
            for resultado in resultados.find_elements(By.CLASS_NAME, "row"):
                nome_advogado = resultado.find_element(By.CLASS_NAME, "rowName").find_elements(By.TAG_NAME, "span")
                inscricao_advogado = resultado.find_element(By.CLASS_NAME, "rowInsc").find_elements(By.TAG_NAME, "span")
                uf_advogado = resultado.find_element(By.CLASS_NAME, "rowUf").find_elements(By.TAG_NAME, "span")

                # Verificando se o UF do lead corresponde ao UF do resultado obtido
                if uf_advogado[-1].text == uf:
                    print(uf, uf_advogado[-1].text)
                    print(f"É advogado(a) {nome_advogado[-1].text.title()} - {inscricao_advogado[-1].text}/{uf_advogado[-1].text}")
                    return True
                else:
                    print("O nome consta, mas não corresponde ao UF.")
                    
            return False
        except:
            print("Não consta na CNA.")
            return False
    except Exception as e:
        print(f"Erro ao verificar CNA: {e}")