import math

def addizione(n1,n2):
    addizione = n1 + n2
    print(f"addizione = {addizione}")

def sottrazione(n1,n2):
    sottrazione = n1 + n2
    print(f"sottrazione = {sottrazione}")

def moltiplicazione(n1,n2):
    moltiplicazione = n1 * n2
    print(f"moltiplicazione = {moltiplicazione}")

def divisione(n1,n2):
    divisione = n1/n2
    if n1 == 0 and n2 == 0:
        print("equazione indeterminata")
    elif n1 !=0 and n2 == 0:
        print("equazione impossibile")

def potenza(n1,n2):
    potenza = n1 ** n2
    print(f"potenza = {potenza}")



def main():
    scelta = int(input("""inserire operazione: 
        1 - addizione
        2 - sottrazione
        3 - moltiplicazione
        4 - divisione
        5 - potenza 
        6 - fine """))


    while True:
        if scelta == 1:
            n1 = int(input("inserire numero 1:"))
            n2 = int(input("inserire numero 2: "))
            addizione(n1,n2)
        elif scelta == 2:
            n1 = int(input("inserire numero 1:"))
            n2 = int(input("inserire numero 2: "))
            sottrazione(n1,n2)
        elif scelta == 3:
            n1 = int(input("inserire numero 1:"))
            n2 = int(input("inserire numero 2: "))
            moltiplicazione(n1,n2)
        elif scelta == 4:
            n1 = int(input("inserire numero 1:"))
            n2 = int(input("inserire numero 2: "))
            divisione(n1,n2)
        elif scelta == 5:
            n1 = int(input("inserire numero 1:"))
            n2 = int(input("inserire numero 2: "))
            potenza(n1,n2)
        else: 
            exit()
main()










main()
        