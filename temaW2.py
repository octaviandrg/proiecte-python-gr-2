lista = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]
print(sorted(lista))
print(sorted(lista, reverse=True))
lista.sort()
sliced_list = lista[1::2]
print(sliced_list)
sliced_list = lista[::2]
print(sliced_list)
for x in lista:
    if x % 3 == 0:
        print(x)
