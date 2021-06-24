import random

tam = 10000      # variavel tamanho da lista
min = 1       # menor numero que pode gerar na lista
max = 5000     # maior numero que pode gerar na lista

def gera_lista_aleatoria(tam, min, max):
    "Função cria lista com números pseudo-aleatórios"
    listaAleatoria = []                   # cria variável de lista aleatória
    for i in range(tam):                  # preenche a lista
        num = random.randint(min, max)    # cria numero aleatorio dentro do min e do max
        listaAleatoria.append(num)        # add numero aleatorio na lista
    return listaAleatoria
