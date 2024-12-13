import math


def potenza(base, esponente):
    pot = base ** esponente
    return pot

def fattoriale(n):
    fatt = 1 

    for i in range(2, n+1):
        fatt = fatt * i
    
    return fatt

def logaritmo(argomento):
    rlog = math.log10(argomento)

    return rlog