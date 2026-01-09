import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import os
from dotenv import load_dotenv

load_dotenv()

filename = "busca-adv-c66ad2a6c75c.json"
scopes = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/drive",
]
creds = ServiceAccountCredentials.from_json_keyfile_name(
    filename=filename,
    scopes=scopes
)
client = gspread.authorize(creds)
folder_id = os.getenv("ID_FOLDER")

planilha_completa = client.open(
    title="Busca ADV",
    folder_id=folder_id,  # O ID da pasta do Drive vai aqui (pegar do link)
    )
planilha = planilha_completa.get_worksheet(0)

def inserir_dados(dados_adv):
    try:
        planilha.append_row(dados_adv, value_input_option="USER_ENTERED")
    except Exception as e:
        print(e)