def statistiche():
    punteggi = []
    punteggio = 0
    somma_punteggi = 0
    c = 0
    punteggi_scarsi = set()
    nuovi_punteggi = []
    while punteggio >= 0:
        punteggio = int(input("inserisci punteggio: "))
        if punteggio < 0:
            exit
        else:
            somma_punteggi = somma_punteggi + punteggio
            c += 1
            punteggi.append(punteggio)
            if punteggio < 50:
                punteggi_scarsi.add(punteggio)
        
    punteggio_minimo = min(punteggi)
    punteggio_massimo = max(punteggi)
    media = somma_punteggi/c
    print(f"punteggio_minimo: {punteggio_minimo}")
    print(f"punteggio massimo: {punteggio_massimo}")
    print(f"media dei punti: {media}")    
    print(f"punteggi scarsi: {punteggi_scarsi}")
    nuovi_punteggi = punteggi
    nuovi_punteggi.sort()
    print(nuovi_punteggi[::-1])

def main():
    statistiche()
main()