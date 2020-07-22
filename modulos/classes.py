# Aplicativo para evangelizar
# vai ser as classes, e funções, para serem aplicadas no app principal


class Pessoa:
    def __init__(self, identificador, nome, dataNas, rua, numCasa, email, senha):
        self.identificador = identificador
        self.nome = nome
        self.dataNas = dataNas
        self.rua = rua
        self.numCasa = numCasa
        self.email = email
        self.senha = senha

    def alterar_nome(self, nome):
        self.nome = nome

    def alterar_data(self, dataNas):
        self.dataNas = dataNas

    def alterar_endereco(self, rua, numCasa):
        self.rua = rua
        self.numCasa = numCasa


class Autor(Pessoa):
    def __init__(self, identificador, nome, dataNas, rua, numCasa, email, senha, formacao, assinatura):
        Pessoa.__init__(self, identificador, nome, dataNas, rua, numCasa, email, senha)
        self.formacao = formacao
        self.assinatura = assinatura

    def __str__(self):
        return self.nome


class Admin(Pessoa):
    def __init__(self, identificador, nome, dataNas, rua, numCasa, email, senha, teste_seguranca):
        Pessoa.__init__(self, identificador, nome, dataNas, rua, numCasa, email, senha)
        self.teste_seguranca = teste_seguranca

    def __str__(self):
        return self.nome


class Usuario(Pessoa):
    def __init__(self, identificador, nome, dataNas, rua, numCasa, email, senha):
        Pessoa.__init__(self, identificador, nome, dataNas, rua, numCasa, email, senha)

    def __str__(self):
        return self.nome


class Postagem:
    def __init__(self, autor, texto, dataCri, dataPub):
        self.autor = autor
        self.texto = texto
        self.dataCri = dataCri
        self.dataPub = dataPub

    def publicar(self, dataPub):
        self.dataPub = dataPub

    def __str__(self):
        return self.autor
