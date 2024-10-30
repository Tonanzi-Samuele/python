def fattoriale(numero):
    fatt = 1
    for i in range(2, numero + 1):
        fatt = fatt*i
        print(fatt)
    
    return fatt