def succ(a):
    for i in range(5):
        a += 1
        print(a)


n = int(input("inserire numero:"))
if n > 0:
    succ(n)
else:
    print("numero non positivo")