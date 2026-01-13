from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def verificar_cna(driver, nome, uf):
    try:
        print(f"Verificando {nome} no CNA...")
        driver.get("https://cna.oab.org.br/")

        wait = WebDriverWait(driver, 15)

        campo_nome = wait.until(EC.presence_of_element_located((By.ID, "txtName")))
        campo_nome.clear()
        campo_nome.send_keys(f'"{nome}"')

        botao_buscar = wait.until(EC.element_to_be_clickable((By.ID, "btnFind")))
        botao_buscar.click()

        try:
            # Espera resultados
            resultados = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.ID, "divResult"))
            )

            # print(resultados)

            for resultado in resultados.find_elements(By.CLASS_NAME, "row"):
                uf_cna = resultado.find_element(By.CLASS_NAME, "rowUf").find_elements(By.TAG_NAME, "span")
                print("UF cna:", uf_cna[-1].text)

                if uf_cna[-1].text == uf:
                    print(f"É advogado(a): {nome} - {uf}")
                    return True
                else:
                    print("O nome consta, mas não corresponde a UF do lead.")
                    return False
        except Exception as e:
            print("Não consta na CNA")
            return False

    except Exception as e:
        print(f"Erro ao verificar CNA: {e}")
        return False