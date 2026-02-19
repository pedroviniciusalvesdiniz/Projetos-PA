import webbrowser

def redirect_wpp(nome, telefone):
    # print(nome)
    # print(telefone)
    
    mensagem = f"Oi, {nome}! Sou da Processo Ágil e vi seu cadastro. Grande parte dos nossos clientes são advogados buscando automatizar a captura de processos e movimentações. É o seu caso?"

    webbrowser.open(f"https://api.whatsapp.com/send?phone={telefone}&text={mensagem.replace(' ', '%20')}")
