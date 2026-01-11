import requests
import os
from dotenv import load_dotenv

BASE_URL = 'http://localhost:8080'
INSTANCE_NAME = os.getenv('INSTANCE_NAME')
AUTHENTICATION_API_KEY = os.getenv('AUTHENTICATION_API_KEY')

url = f"{BASE_URL}/message/sendText/{INSTANCE_NAME}"

headers = {
    'apikey': AUTHENTICATION_API_KEY,
    'Content-Type': 'application/json'
}

def send_wpp(numero, nome):
    payload = {
        'number': numero,
        'textMessage': {
            "text": f"Olá {nome.split()[0]}! Sou Vinicius da Processo Ágil. Notei que você se cadastrou na nossa plataforma. Você está com alguma dúvida?"
        },
        'delay': 10000
    }

    try:
        response = requests.post(url, headers=headers, json=payload)
        return response.json()
    except Exception as e:
        print(f"Erro ao enviar mensagem: {e}")
        return None
