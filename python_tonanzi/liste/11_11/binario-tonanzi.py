def binario(n):
    if n!=0:
        binario(n//2)
        print(n%2, end=' ')

def main():
    n = 0
    while n <= 0:
        n = int(input("inserire numero da convertire: "))
    binario(n)
main()