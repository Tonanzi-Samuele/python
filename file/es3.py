def main():
    try:
        with open("testo.txt", "r") as file:
            cont = file.read()
        with open("copia.txt","w") as cp:
            cp.write(cont)
            print("contenuto copiato")
    except FileNotFoundError:
        print("file inesistente")
main()