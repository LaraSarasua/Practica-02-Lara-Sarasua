def validar_email(email):
    if email.count("@") != 1:
        return False
    if email.startswith("@") or email.endswith("@") or email.startswith("..") or email.endswith(".."):
        return False
    
    partes = email.split("@")
    local = partes[0]
    dominio = partes[1]

    if local == "" or dominio == "":
        return False
    
    if "." not in dominio:
        return False
    
    partes_dominio = dominio.split(".")
    ultima_parte = partes_dominio[-1]
    if len(ultima_parte) < 2:
        return False
    
    return True