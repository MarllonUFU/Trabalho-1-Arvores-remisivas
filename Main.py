import re
import time
from avl import AVL

def normalizar(p):
    return re.sub(r"[^\wáéíóúãõâêôç]", "", p.lower())

def main():
    avl = AVL()
    total = 0
    repetidas = 0

    inicio = time.time()

    with open("texto_origem.txt", encoding="utf-8") as f:
        for i, linha in enumerate(f, start=1):
            palavras = linha.split()
            for p in palavras:
                palavra = normalizar(p)
                if palavra:
                    total += 1
                    antes = len(avl.busca_prefixo(palavra))
                    avl.inserir(palavra, i)
                    depois = len(avl.busca_prefixo(palavra))
                    if depois == antes:
                        repetidas += 1

    fim = time.time()

    distintas = total - repetidas
    stats = {
        "Total de palavras": total,
        "Total de palavras distintas": distintas,
        "Total de palavras descartadas": repetidas,
        "Tempo de construção": f"{fim - inicio:.4f}s",
        "Total de rotações": avl.rotacoes
    }

    avl.imprimir_indice("indice.txt", stats)

    print("Índice gerado com sucesso!")
    print("Palavra mais frequente:", avl.palavra_mais_frequente())

    # Exemplo de busca
    termo = "alg"
    print("Busca por prefixo:", avl.busca_prefixo(termo))

if __name__ == "__main__":
    main()
