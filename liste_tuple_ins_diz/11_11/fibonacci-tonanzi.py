def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)


def main():
    n = int(input("inserire numero: "))
    for i in range(n):
        print(fib(i))
main()