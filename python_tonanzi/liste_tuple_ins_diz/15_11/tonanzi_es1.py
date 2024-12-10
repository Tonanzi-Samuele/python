import random
MAX = random.randint(0,100)
v = [0]*MAX
somma = 0

for i in range(len(v)):
    v[i] = random.randint(1,100)
    somma += v[i]
print(v)
print(somma)