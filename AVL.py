from no import NoAVL

class AVL:
    def __init__(self):
        self.raiz = None
        self.rotacoes = 0

    def altura(self, no):
        return no.altura if no else 0

    def atualizar(self, no):
        no.altura = 1 + max(self.altura(no.esq), self.altura(no.dir))
        no.qtd_subarvore = 1 + self.contar(no.esq) + self.contar(no.dir)

    def contar(self, no):
        return no.qtd_subarvore if no else 0

    def fator_balanceamento(self, no):
        return self.altura(no.esq) - self.altura(no.dir)

    def rot_dir(self, y):
        self.rotacoes += 1
        x = y.esq
        t2 = x.dir
        x.dir = y
        y.esq = t2
        self.atualizar(y)
        self.atualizar(x)
        return x

    def rot_esq(self, x):
        self.rotacoes += 1
        y = x.dir
        t2 = y.esq
        y.esq = x
        x.dir = t2
        self.atualizar(x)
        self.atualizar(y)
        return y

    def inserir(self, palavra, linha):
        self.raiz = self._inserir(self.raiz, palavra, linha)

    def _inserir(self, no, palavra, linha):
        if not no:
            return NoAVL(palavra, linha)

        if palavra < no.palavra:
            no.esq = self._inserir(no.esq, palavra, linha)
        elif palavra > no.palavra:
            no.dir = self._inserir(no.dir, palavra, linha)
        else:
            no.linhas.add(linha)
            return no

        self.atualizar(no)
        fb = self.fator_balanceamento(no)

        if fb > 1 and palavra < no.esq.palavra:
            return self.rot_dir(no)
        if fb < -1 and palavra > no.dir.palavra:
            return self.rot_esq(no)
        if fb > 1 and palavra > no.esq.palavra:
            no.esq = self.rot_esq(no.esq)
            return self.rot_dir(no)
        if fb < -1 and palavra < no.dir.palavra:
            no.dir = self.rot_dir(no.dir)
            return self.rot_esq(no)

        return no

    def buscar(self, palavra):
        no = self.raiz
        while no:
            if palavra == no.palavra:
                me = self.contar(no.esq) - self.contar(no.dir)
                if me == 0:
                    return 0
                else:
                    print(f"ME = {me}")
                    return 1
            no = no.esq if palavra < no.palavra else no.dir
        return -1

    def busca_prefixo(self, prefixo):
        resultado = []
        self._prefixo(self.raiz, prefixo, resultado)
        return resultado

    def _prefixo(self, no, prefixo, res):
        if not no:
            return
        if no.palavra.startswith(prefixo):
            res.append(no.palavra)
        if prefixo <= no.palavra:
            self._prefixo(no.esq, prefixo, res)
        self._prefixo(no.dir, prefixo, res)

    def palavra_mais_frequente(self):
        melhor = ["", 0]
        self._mais_frequente(self.raiz, melhor)
        return melhor[0], melhor[1]

    def _mais_frequente(self, no, melhor):
        if not no:
            return
        if len(no.linhas) > melhor[1]:
            melhor[0] = no.palavra
            melhor[1] = len(no.linhas)
        self._mais_frequente(no.esq, melhor)
        self._mais_frequente(no.dir, melhor)

    def imprimir_indice(self, arq, stats):
        with open(arq, "w", encoding="utf-8") as f:
            self._inorder(self.raiz, f)
            f.write("\n")
            for k, v in stats.items():
                f.write(f"{k}: {v}\n")

    def _inorder(self, no, f):
        if not no:
            return
        self._inorder(no.esq, f)
        linhas = ",".join(map(str, sorted(no.linhas)))
        f.write(f"{no.palavra} {linhas}\n")
        self._inorder(no.dir, f)
