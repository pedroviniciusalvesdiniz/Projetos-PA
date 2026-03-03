# from take_info_lead import criar_driver
# from take_info_lead import entry_account

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

def creating_event(driver, dados):
    # driver = criar_driver()

    # entry_account(driver)
    # driver.get("https://processoagil.com/softurbano")
    try:

        
        driver.get("https://bernerspa.processoagil.com/Sistema/Planejamento/Agenda.aspx")
        wait = WebDriverWait(driver, 20)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="AgendaConteudoAgenda"]/div/div/div/div[1]/div[2]/a'))).click()

        # wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="aspnetForm"]/div[3]/div[11]/div[2]/div/div/div[1]/div/div[1]/ul/li/div/a'))).click()

        # print(dados["nome"])
        # print(dados["telefone"])

        wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="MasterPageDivInserirEvento_InpResumoTituloEvento"]'))).send_keys(f"Abordagem 1 - {dados["nome"]} - {dados["telefone"]}")

        wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="SeletorArvoreTagVaziaMasterPageDivInserirEvento_divResumoEixoEstrategico"]/span'))).click()

        wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="SeletorArvoreImgAbreFechaMasterPageDivInserirEvento_divResumoEixoEstrategicoeacc39e0-7e53-4bed-93e0-1c8c3ce4d8e7"]'))).click()

        wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="SeletorArvoreImgAbreFechaMasterPageDivInserirEvento_divResumoEixoEstrategico4b17045d-2e8b-46a3-854e-c1dff4342425"]'))).click()

        wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="SeletorArvoreSpnOpcaoMasterPageDivInserirEvento_divResumoEixoEstrategico16dce80e-160e-482d-91b3-e7e0f9465e28"]'))).click()

        wait.until(EC.element_to_be_clickable((By.ID, 'MasterPageDivInserirEvento_ResumoSlcFaseEvento'))).click()
        wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="MasterPageDivInserirEvento_ResumoSlcFaseEvento"]/option[9]'))).click()

        time.sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="MasterPageDivInserirEvento_novaTarefaLiteAreaDescricao"]/p'))).send_keys(f"{dados['cpf']} - {dados['email']} - {dados['uf']} - {dados['isLawer']}")

        wait.until(EC.element_to_be_clickable((By.ID, 'MasterPageDivInserirEvento_InpInserirEvento'))).click()

        time.sleep(2)

        print("Evento criado com sucesso.")
    except Exception as e:
        print(f"Erro ao criar evento: {e}")
