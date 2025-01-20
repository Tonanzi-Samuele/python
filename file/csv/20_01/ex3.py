import csv 


def main():
    try:
        with open("numeri.csv",mode ="r", encoding="utf-8") as file:
            contenuto = file.read()
        cont_int = [int(n) for n in contenuto.split()[1:]]
        print("la somma è: ", sum(cont_int))
    except FileNotFoundError:
        print("errore")
main()