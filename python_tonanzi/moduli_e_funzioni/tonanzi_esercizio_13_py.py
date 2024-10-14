import pitagora


x1  = int(input("inserire coordinate 1 punto x: "))
y1  = int(input("inserire coordinate 1 punto y: "))


x2  = int(input("inserire coordinate 2 punto x: "))
y2  = int(input("inserire coordinate 2 punto y: "))

print(f"distanza tra i due punti è = {pitagora.dist(x1,y1,x2,y2)} ")