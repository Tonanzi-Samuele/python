from math import pi
class Cerchio():

    def __init__(self,raggio = 0):
        self.raggio = raggio
        while self.raggio < 0:
            self.raggio = int(input("inserire raggio: "))
    def calcola_area(self):
        A = (self.raggio**2) * pi
        self.area = A
        return self.area
    def calcola_perimetro(self):
        P = (self.raggio*2)*pi
        self.P = P
        return self.P


        
            
        