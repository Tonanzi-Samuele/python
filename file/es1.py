def main():
    fout = open('amici.txt','w')
    print("inserisci amici, uno per riga")
    nome = input("nome inserire * per finire: ").strip()
    while nome != "*":
        fout.write(nome +"\n")
        nome = input("nome inserire * per finire: ").strip()
    print("ballin'")
    fout.close()
    
main()