class Rettangolo(object):
    base = 0.0
    alt = 0.0

    def assegna(self,b,h):
        self.base = b
        self.alt = h

    def area(self):
        return self.base * self.alt
    
    def perimetro(self):
        return self.base * 2 + self.alt * 2



def main():
    tovaglia = Rettangolo()
    tavolo = Rettangolo()
    b = int(input("inserire base: "))
    h = int(input("inserire altezza: "))
    b_tavolo = int(input("inserire base: "))
    h_tavolo = int(input("inserire altezza: "))
    tovaglia.assegna(b,h)
    tavolo.assegna(b_tavolo,h_tavolo)

    print(f"""
area = {tovaglia.area()}
perimetro = {tovaglia.perimetro()}



area = {tavolo.area()}
perimetro = {tavolo.perimetro()}""") 
main()



