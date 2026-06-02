class Cliente:

    def __init__(self, nome, cpf, telefone=None, email=None):

        self.__nome = None
        self.__cpf = None
        self.__telefone = None
        self.__email = None

        if validar_nome(nome):
            self.__nome = nome

        if validar_cpf(cpf):
            self.__cpf = somente_digitos(cpf)

        if telefone is not None and validar_telefone(telefone):
            self.__telefone = somente_digitos(telefone)

        if email is not None validar_email(email):
          self.__ 
