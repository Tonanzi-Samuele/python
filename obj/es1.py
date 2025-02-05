class Calcolatrice(object):
    def somma(self,a,b):
        self.a = a
        self.b = b
        return self.a + self.b
    def sottr(self,a,b):
        self.a = a
        self.b = b
        return self.a -  self.b
    def molt(self,a,b):
        self.a = a
        self.b = b
        return self.a * self.b
    def divisione(self ,a,b):
        self.a = a
        self.b = b
        return self.a / self.b

def main():
    calc = Calcolatrice()
    print("""\
    1 - somma
    2 - sottrazione
    3 - moltiplicazione
    4 - divisione""")
    scelta = int(input("inserire scelta: "))
    match(scelta):
        case 1:
            a = int(input("inserire n1: "))
            b = int(input("inserire n2: "))
            print(f"somma = {calc.somma(a,b)}")
        
        case 2:
            a = int(input("inserire n1: "))
            b = int(input("inserire n2: "))
            print(f"sottrazione = {calc.sottr(a,b)}")
        
        case 3:
            a = int(input("inserire n1: "))
            b = int(input("inserire n2: "))
            print(f"moltiplicazione = {calc.molt(a,b)}")
        
        case 4:
            a = int(input("inserire n1: "))
            b = int(input("inserire n2: "))
            if b == 0:
                print("impossibile")
            else:
                print(f"divisione = {calc.divisione(a,b)}")

main()