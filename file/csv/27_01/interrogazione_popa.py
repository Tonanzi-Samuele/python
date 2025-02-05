import csv
from collections import defaultdict

def salvare():
    try:
        with open("file.csv", mode = "a",encoding= "utf-8")as file: 
            
            intestazione = ["User", "password", "email", "data"]
            writer = csv.DictWriter(file, fieldnames = intestazione)    
            writer.writeheader()
            scelta = {}
            scelta["User"] = str(input("inserire nome user: "))
            scelta["password"] = str(input("inserire password: "))
            scelta["email"] = str(input("inserire email: "))
            scelta["data"] = str(input("inserire data: "))
            writer.writerow(scelta)
            file.close()
    except FileNotFoundError:
        print("file non trovato")
    #print("ciao")

def leggere():
    print("hello")
    try: 
        with open("file.csv", mode = "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                print(row)
            file.close()
    except FileNotFoundError:
        print("file non trovato")  
def main():
    scelta = 0
    while True:
        scelta = int(input("""
            inserire scelta:
            1 - salvare
            2 - leggere
            3 - terminare   """))
        if scelta == 1:
            salvare()
        elif scelta == 2:
            leggere()
        elif scelta == 3:
            break
    print("terminato")
main()