import webbrowser

def redirect_wpp(nome, telefone):
    # print(telefone)
    mensagem = f"Oi, {nome}. Sou da Processo Ágil. Vi seu cadastro e queria entender: o que te levou a buscar a plataforma?"
    webbrowser.open(f"https://api.whatsapp.com/send?phone={telefone}&text={mensagem.replace(' ', '%20')}")
