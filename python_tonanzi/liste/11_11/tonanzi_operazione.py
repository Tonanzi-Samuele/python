def somma(lista):
    print(sum(lista))

def maxi(lista):
    print(max(lista))


def ordina(lista):
    print(sorted(lista))


def rim_dup(lista):
    lista_nodup = []
    for elemento in lista:
        if elemento not in lista_nodup:
            lista_nodup.append(elemento)
    print(lista_nodup)

def media(lista):
    print(sum(lista)/len(lista))

def cerca(lista):
 n = int(input("inserire numero da cercare: "))
 print(n in lista)

def cont(lista):
    n = int(input("inserire numero da cercare: "))
    lista.count(n)

def inv(lista):
    print(lista[::-1])
    


