class NoAVL:
    def __init__(self, palavra, linha):
        self.palavra = palavra
        self.linhas = set([linha])
        self.esq = None
        self.dir = None
        self.altura = 1
        self.qtd_subarvore = 1  # usado para ME
