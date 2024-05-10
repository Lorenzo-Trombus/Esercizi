def filtra(lista: list[int], fattore: int):
    new_list = []
    for l in lista:
        if l % 2 == 0:
            l *= fattore
            new_list.append(l)

    return new_list

lista = [1, 2, 3, 4, 5, 6]
print(filtra(lista, 3))