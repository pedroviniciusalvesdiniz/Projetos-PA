import webbrowser

def redirect_wpp(nome, telefone):
    # print(telefone)
    mensagem = f"Oi, {nome}. Sou da Processo Ágil. Vi seu cadastro e queria entender: O que te levou a buscar nossa plataforma?"
    webbrowser.open(f"https://api.whatsapp.com/send?phone={telefone}&text={mensagem.replace(' ', '%20')}")
