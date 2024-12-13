import modulo_es1 as calc

x1 = int(input("inserire x di A: "))
y1 = int(input("inserire y di A: "))
x2 = int(input("inserire x di B: "))
y2 = int(input("inserire y di B: "))

distanza = calc.calcola_distanza(x1,y1,x2,y2)
print(f"la distanza tra i due punti è: {distanza}")