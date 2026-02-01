# Índice Remissivo com Árvore AVL

## Introdução
Este projeto implementa um índice remissivo utilizando uma árvore AVL, garantindo ordenação alfabética, balanceamento automático e operações eficientes de inserção, busca e remoção. Cada palavra do texto é armazenada junto com as linhas em que aparece.

## Estruturas de Dados
Foi utilizada uma árvore AVL, onde cada nó contém:
- Palavra
- Conjunto de linhas
- Ponteiros para subárvores esquerda e direita
- Altura
- Contador de nós da subárvore (para cálculo do ME)

## Funcionalidades
- Inserção automática de palavras
- Busca com Medidor de Equilíbrio (ME)
- Busca por prefixo
- Palavra mais frequente
- Impressão do índice em arquivo texto
- Contagem de rotações
- Estatísticas finais

## Exemplos de Uso
```python
avl.inserir("algoritmo", 10)
print(avl.busca_prefixo("alg"))
print(avl.buscar("algoritmo"))
