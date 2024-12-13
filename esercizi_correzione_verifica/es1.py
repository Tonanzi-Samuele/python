fatt = 1
n = 1

while n != 0:
    n = int(input("inserire numero"))
    if n % 2 == 0:
        for i in range(1, n-1):
            fatt = fatt * i
        print(f"fattoriale di {n} = {fatt}")
    else: 
        print("numero dispari")