import random
def somma(lunghezza, matrix):
    scolonna = 0
    sriga = 0
    for i in range(lunghezza):
        for j in range(lunghezza):
            scolonna += matrix[j][i]
            sriga += matrix[i][j]
        print("colonna: ",scolonna, "riga: ",sriga)


def main():
     
    l = random.randint(3,8)
    matrix = []
    for i in range(l):
        riga = []
        for j in range(l):
            n = random.randint(1,10)
            riga.append(n)
        matrix.append(riga)

    somma(l,matrix)
    # matrix.append(lista)
    print(matrix)
main()