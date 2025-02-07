try:
    with open("file.txt", mode = "a") as file:
        elemento = str(input("inserire nome: "))
        while elemento != "":
            file.write(elemento)
            elemento = str(input("Inserire nome:"))
    file.close()

    with open("file.txt", mode = "r") as file:
        reader = file.read()
        
        for riga in reader:
            print(riga, end = "")

except FileNotFoundError:
    with open("file.txt", mode = "a") as file:
        
        elemento = str(input("inserire nome: "))
        while elemento != "":
            file.write(elemento)
            elemento = str(input("inserire nome: "))
    file.close()

    with open("file.txt", mode = "r") as file:
        reader = file.read()
        
        for riga in reader:
            print(riga, end = "")