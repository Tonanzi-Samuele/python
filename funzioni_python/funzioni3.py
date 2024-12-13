def media(som,count):
    media = float(som/count)
    print(media)

def main():
    somma = 0
    c = int(input("inserire contatore: "))
    for i in range(c):
        n = int(input("inserire numero: "))
        somma += n    
    media(somma,c)
main()