def  fatt(n):
    if n==0:
        return 1
    else:
        return n*fatt(n-1)
    

def main():
    n = int(input("inserire numero: "))
    print(f"fattoriale di {n} è = {fatt(n)}")
main()
