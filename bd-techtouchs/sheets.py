import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from dotenv import load_dotenv
import os

load_dotenv()

filename = os.getenv("FILENAME_CREDENTIALS")
scopes = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name(
    filename=filename,
    scopes=scopes
)
client = gspread.authorize(creds)

planilha_completa = client.open(
    title="BD Tech Touchs",
    folder_id="1Cbg0xSdW01hxn3xGivnBT6_s8IfT5ty0",  # O ID da pasta do Drive vai aqui (pegar do link)
    )
planilha = planilha_completa.get_worksheet(0)

def inserir_dados(dados_lead):
    try:
        planilha.append_row(dados_lead, value_input_option="USER_ENTERED")
        print("Sucesso: Lead inserido na TabelaLeads")
    except Exception as e:
        print("Erro: Não foi possível inserir o lead na TabelaLeads", e)