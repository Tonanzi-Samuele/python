scacchiera = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]


def somma_diagonali(scacchiera):
    somma = 0
    somma_reverse = 0
    for i in range(0,3,1):
        for j in range(0,3,1):
            if i == j:
                somma += scacchiera[i][j]
    print(somma)
    for i in range(2,-1,-1):
        for j in range(len(scacchiera)):
            if i == j:
                somma_reverse += scacchiera[i][j]
    print(somma_reverse)

somma_diagonali(scacchiera) 