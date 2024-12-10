quant = int(input("quanti numeri si vogliono inserire: "))
lista_num = []
nuova_lista = []
for i in range(quant):
    n = int(input("inserire numero"))
    lista_num.append(n)


print(f"lista iniziale: {lista_num}")
for i in range(len(lista_num)):
    if lista_num[i] >= 100:
        var = lista_num[i] * 3 
        nuova_lista.append(var)
    else:
        v = lista_num[i] * 2
        nuova_lista.append(v)


print(f"lista nuova: {nuova_lista}")