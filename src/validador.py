def somente_digitos(texto):
    return ''.join(c for c in texto if c.isdigit())


def validar_nome(nome):
    return nome is not None and len(nome.strip()) >= 5


def validar_cpf(cpf):
    if cpf is None:
        return False

    cpf_ok = somente_digitos(cpf)
    return len(cpf_ok) == 11


def validar_telefone(telefone):
    if telefone is None:
        return False
    
    telefone_ok = somente_digitos(telefone)
    return len(telefone_ok) == 11

def validar_email(email):
    if email is None:
        return False

    return '@' in email

def validar_numero_positivo(numero):
    return numero > 0
