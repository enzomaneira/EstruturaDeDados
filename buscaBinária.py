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



def busca_binaria(lista, item):
    "Função retorna posição de número recebido"
    low = 0                           # determina menor posição da lista
    high = len(lista) - 1             # determina maior posição da lista
    while low <= high:                # enquanto menor posição for menor ou igual que maior posição loop é executado
        mid = ((low + high) / 2)      # meio = (menor posição + maior posição) / 2
        mid = round(mid)              # arredonda meio
        busca = lista[mid]            # busca numero procurado no meio
        if busca == item:             # se numero procurado foi achado retorna posição
            return mid
        if busca > item:              # se numero procurado é menor que a posição de busca, high vira uma posição
            high = mid - 1            # a menos que o mid
        if busca < item:              # se numero procurado é maior que a posição de busca low vira uma posição
            low = mid + 1             # a mais que o mid
    return None

lista = gera_lista_aleatoria(tam, min, max)
print(f'Lista Aleatória: {lista}')
listaOrder = bubble_sort(lista)
print(f'Lista Ordenada: {listaOrder}')
item = int(input(f'Qual número retornar a posição?\n'))
print(busca_binaria(listaOrder, item))