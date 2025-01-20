def contaparole(fout):
    f = fout.read()
    n = f.split(" ")
    return n
def main():
    try:
        with open('testo.txt', 'r') as fout:
            n  = contaparole(fout)
            print(len(n))
    except FileNotFoundError:
        print("file non esistente")

main()