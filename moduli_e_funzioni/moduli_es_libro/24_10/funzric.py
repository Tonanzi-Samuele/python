# fattoriale.py: fattoriale n! di un numero n
# funzione ricorsiva per il calcolo del fattoriale
def fatt(x):
if x == 0:
f = 1
else:
f = x * fatt(x-1)
return f
# funzione principale
def main():
n = int(input("Numero naturale: "))
print("Fattoriale del numero", n, "=", fatt(n))
# istruzione di avvio del programma
main()