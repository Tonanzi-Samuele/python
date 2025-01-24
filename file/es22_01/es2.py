def main():
    lista_i = []
    n = int(input("inserire dimensione lista: "))
    if n > 0 and n < 11:
        for i in range(n):
            elem = int(input("inserire numero: "))
            if elem > -101 and elem < 101:
                lista_i.append(elem)
            else:
                print("errore")
                break
    else:
        print("errore")
        exit    
    print(f"lista con duplicati = {lista_i}")
    lista_senza_duplicati = set(lista_i)
    print(f"insieme senza duplicati = {lista_senza_duplicati}")
    
main()