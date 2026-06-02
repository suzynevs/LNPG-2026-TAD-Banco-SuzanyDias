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
          self.__email = email 

    def get_nome(self):
        return self.__nome

    def get_cpf(self):
        return self.__cpf

    def get_telefone(self):
        return self.__telefone

    def get_email(self):
        return self.__email

    def alterar_telefone(self, telefone):
        if validar_telefone(telefone):
            self.__telefone = somente_digitos(telefone)

    def alterar_email(self, email):
        if validar_email(email):
            self.__email = email
