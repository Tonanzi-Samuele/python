def cerca_comune(lista):
    c = 0   
    cerc = str(input("inserire comune da cercare:"))
    for elemento in range(len(lista)):
        if lista[elemento] == cerc:
            c += 1 
    print(f"il comune appare {c} volte")
def main():
    comuni = int(input("inserire quanti comuni si voglioni inserire: "))
    lista_comuni = []

    for i in range(comuni):
        comune = str(input("inserire comune:"))
        lista_comuni.append(comune)
        
    cerca_comune(lista_comuni)

main()





