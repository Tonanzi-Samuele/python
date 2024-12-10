stringa = str(input("inserire stringa: "))
punteggiatura = "!,.:?"
for i in punteggiatura:
    stringa = stringa.lower()
    stringa = stringa.replace(i,"")
lista_par = set(stringa.split())
print(lista_par)