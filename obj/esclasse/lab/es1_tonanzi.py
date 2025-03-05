class Build:
    def __init__(self,stanze = 0,superficie = 0,indirizzo = "",citta = ""):
        self.stanze = stanze
        self.superf = superficie
        self.ind = indirizzo
        self.citta = citta
    def __str__(self):
        return f"stanze = {self.stanze}, superficie = {self.superf}, indirizzo = {self.ind}, citta = {self.citta}"
class Apt(Build):
    def __init__(self, stanze, superficie, indirizzo, citta, piano = "",ascensore = True,terrazzi = 0):
        super().__init__(stanze, superficie, indirizzo, citta)
        self.piano = piano
        self.ascensore = ascensore
        self.terrone = terrazzi
    def __str__(self):
        return super().__str__() + f"piano = {self.piano}, ascensore {'Presente' if self.ascensore == True else "non presente"}"
class Villa(Build):
    def __init__(self, stanze, superficie, indirizzo, citta, piani = 0, supergiard = 0, piscia = True):
        super().__init__(stanze, superficie, indirizzo, citta)
        self.piani = piani
        self.sup = supergiard
        self.pisci = piscia
    def __str__(self):
        return super().__str__() + f"piani = {self.piani}, superficie del giardino = {self.sup}, piscina = {'Presente' if self.pisci == True else "non presente"}"
class Test():
    def main():
        casa = Villa(5,20,"via","nichelino",3,6,True)
        asac = Apt(5,20,"via","torino",3,6,False)
        print(casa)
        print(asac)
    
    main()

ciao = Test()
ciao.main
