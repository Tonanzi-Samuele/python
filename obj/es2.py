class Persona(object):
    def __init__(self,nome,eta):
        self.nome = nome
        self.eta = eta
    def pres(self):
        print(f"sono {self.nome} e ho {self.eta} anni")
    def mod_eta(self):
        n_eta = int(input("inserire nuova eta: "))
        self.eta = n_eta

nome = str(input("inserire nome: "))
eta  = int(input("inserire eta: "))
pers = Persona(nome,eta)
pers.pres()
pers.mod_eta()
