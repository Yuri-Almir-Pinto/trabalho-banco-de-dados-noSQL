class Info:

    def __init__ (self, descricao = None, link = None):
        self.descricao = descricao
        self.link = link

class Alternativas:

    def __init__ (self, enunciado, correta):
        self.enunciado = enunciado
        self.correta = correta

class Prova:

    def __init__ (self, cargo, ano, orgao, instituicao, nivel, questoes, id=None):
        self.cargo = cargo
        self.ano = ano
        self.orgao = orgao
        self.instituicao = instituicao
        self.nivel = nivel
        self.questoes = questoes
        self.id = id

class Questoes:

    def __init__ (self, topicos, enunciado, alternativas, textos = Info(None, None), imagens = Info(None, None), id = None):
        self.topicos = topicos
        self.enunciado = enunciado
        self.alternativas = alternativas
        self.textos = textos
        self.imagens = imagens
        self.id = id

