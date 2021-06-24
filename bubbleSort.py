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

def bubble_sort(lista):
    "função de ordenação de lista"
    troca = True                                                     # troca verdadeira para executar looping
    while troca:                                                     # enquanto troca for verdade executa looping
        troca = False                                                # troca vira falso
        for i in range(len(lista) - 1):                              # percorre a lista até a última posição
            if lista[i] > lista[i + 1]:                              # se numero anterior for maior que o proximo numero
                lista[i], lista[i + 1] = lista[i + 1], lista[i]      # numeros trocam de posição
                troca = True                                         # troca volta a ser true para recomeçar função
    return lista

