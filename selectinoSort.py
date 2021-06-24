def selectionSort(lista):
    novaLista = []
    for i in range(len(lista)):
        menor = lista[0]
        indexMenor = 0
        for i in range(1, len(lista)):
            if lista[i] < menor:
                menor = lista[i]
                indexMenor = i
        menor = indexMenor
        novaLista.append(lista.pop(menor))
    return novaLista

print(selectionSort([5, 3, 6, 2, 10]))
