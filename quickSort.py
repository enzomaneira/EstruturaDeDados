import random

tam = 10      # variavel tamanho da lista
min = 1       # menor numero que pode gerar na lista
max = 5000     # maior numero que pode gerar na lista

def gera_lista_aleatoria(tam, min, max):
    "Função cria lista com números pseudo-aleatórios"
    listaAleatoria = []                   # cria variável de lista aleatória
    for i in range(tam):                  # preenche a lista
        num = random.randint(min, max)    # cria numero aleatorio dentro do min e do max
        listaAleatoria.append(num)        # add numero aleatorio na lista
    return listaAleatoria

array = gera_lista_aleatoria(tam, min, max)
print(array)


def quicksort(array):
    if len(array) < 2:         # se array for menor que 2
        return array           # retorna array
    else:
        pivot = array[0]       # define pivo como primeiro elemento do array
        less = [i for i in array[1:] if i <= pivot]         # joga elemento menor que pivo em outro array
        greater = [i for i in array[1:] if i > pivot]       # joga elemento maior que pivo em outro array
        return quicksort(less) + [pivot] + quicksort(greater)      # soma lista do menores com pivo e lista dos maiores

print(quicksort(array))
