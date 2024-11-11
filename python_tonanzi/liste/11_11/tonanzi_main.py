import tonanzi_operazione as calc

lungh = int(input("inserire la lunghezza della lista: "))
lista = []

for i in range(lungh):
    n = int(input("inserire numeri staccati da uno spazio: "))
    lista.append(n)



print("""\
1. somma
2. valore max
3. ordinare la lista
4. rimuovere i duplicati
5. media
6. cercare un elemento
7. contare frequenza numero
8. invertire la lista""")
scelta = int(input("inserire scelta: "))
match scelta:
    case 1:
        calc.somma(lista)
    case 2:
        calc.maxi(lista)
    case 3: 
        calc.ordina(lista)
    case 4:
        calc.rim_dup(lista)
    case 5:
        calc.media(lista)
    case 6:
        calc.cerca(lista)
    case 7:
        calc.cont(lista)
    case 8:
        calc.inv(lista)
