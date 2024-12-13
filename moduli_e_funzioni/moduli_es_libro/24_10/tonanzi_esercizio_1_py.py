import calc 

print("""\
1 - potenza
2 - fattoriale
3 - logaritmo 

""")
scelta = int(input("inserire scelta: "))
if scelta == 1:
    base = int(input("inserire base: "))
    esp = int(input("inserire esponente: "))
    print(calc.potenza(base, esp))
elif scelta == 2:
    n = int(input("inserire numero: "))
    print(calc.fattoriale(n))
elif scelta == 3:
    arg = int(input("inserire argomento: "))
    print(calc.logaritmo(arg))
