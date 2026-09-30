def validar_resposta(resposta):
    
    if not resposta:
        return False

    return True


def resposta_correta(resposta, resposta_certa):
   
    return resposta == resposta_certa


def validar_nome(nome):
    
    nome = nome.strip()

    if nome == "":
        return False

    if len(nome) < 2:
        return False

    return True


def validar_pergunta(pergunta):
    
    campos = ["pergunta", "opcoes", "resposta"]

    for campo in campos:
        if campo not in pergunta:
            return False

    if len(pergunta["opcoes"]) != 4:
        return False

    if pergunta["resposta"] not in pergunta["opcoes"]:
        return False

    return True