class Quadrato():
    def __init__(self,lato = 0,perimetro = 0, area = 0):
        self.lato = lato
        self.area = area
        self.perimetro = perimetro
    def Area(self):
        self.area = self.lato * self.lato
        print(f"Area: {self.area}")
    def Perimetro(self):
        self.perimetro = self.lato * 4
        print( f"Perimetro: {self.perimetro}")
        



def main():
    lato = int(input("inserire lato"))
    if lato > 0:
        quad = Quadrato(lato)
        quad.Area()
        quad.Perimetro()
    else:
        print("errore")
main()
    

        