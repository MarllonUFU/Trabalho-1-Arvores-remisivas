import re
import time
from avl import AVL

def normalizar(p):
    return re.sub(r"[^\wáéíóúãõâêôç]", "", p.lower())

def main():
    avl = AVL()
    total = 0
    palavras_distintas = set()
    palavras_repetidas = 0

    inicio = time.time()

    with open("texto_origem.txt", encoding="utf-8") as f:
        for i, linha in enumerate(f, start=1):
            palavras_linha = set()
            for p in linha.split():
                palavra = normalizar(p)
                if palavra:
                    total += 1

                    if palavra in palavras_distintas:
                        palavras_repetidas += 1
                    else:
                        palavras_distintas.add(palavra)

                    avl.inserir(palavra, i)
                    palavras_linha.add(palavra)

    fim = time.time()

    stats = {
        "Total de palavras": total,
        "Total de palavras distintas": len(palavras_distintas),
        "Total de palavras descartadas": palavras_repetidas,
        "Tempo de construção": f"{fim - inicio:.4f}s",
        "Total de rotações": avl.rotacoes
    }

    avl.imprimir_indice("indice.txt", stats)

    print("Índice gerado com sucesso!")
    print("Palavra mais frequente:", avl.palavra_mais_frequente())

    termo = "alg"
    print("Busca por prefixo:", avl.busca_prefixo(termo))

    # Exemplo de busca com ME
    palavra_busca = "amor"
    res = avl.buscar(palavra_busca)
    if res == -1:
        print(f"'{palavra_busca}' não encontrada.")
    elif res == 0:
        print(f"'{palavra_busca}' encontrada. ME = 0 (equilibrado).")
    else:
        print(f"'{palavra_busca}' encontrada. ME diferente de zero.")

if __name__ == "__main__":
    main()
import os
print("\nAbrindo indice.txt automaticamente...")
os.startfile("indice.txt")
