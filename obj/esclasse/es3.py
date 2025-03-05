class Persona:
   
    def assegna(self, nome = "", cognome = "", codicefiscale = ""):
        self.nome = nome
        self.cognome = cognome
        self.codicefiscale = codicefiscale
    
    def mostra(self):
        print(f"""\
\n------------------------------
NOME, COGNOME E CODICE FISCALE
------------------------------
Nome persona: {self.nome}
Cognome persona: {self.cognome}
Codice Fiscale: {self.codicefiscale}\n\n""")

class Studente(Persona):
    def __init__(self, nome = "", cognome = "", codicefiscale = "",matricola = "", uni = ""):
        super().__init__(nome,cognome,codicefiscale)

    def assegna_matricola(self, matricola):
        self.matricola = matricola
    
    def assegna_universita(self, uni):
        self.uni = uni
    
    def mostra(self):
        print(f"""\
\n-----------------------
MATRICOLE E UNIVERSITA'
-----------------------
Matricola: {self.matricola}
Università: {self.uni}\n\n""")

class Docente(Persona):
    def __init__(self, nome = " ", cognome = "", codicefiscale = "",salario = "", mater = ""):
        super().__init__()
    
    def assegna_salario(self,salario):
        self.salario = salario
    
    def assegna_materia(self,mater):
        self.mater = mater
    
    def mostra(self):
        print(f"""\
\n-----------------------
MATRICOLE E UNIVERSITA'
-----------------------
Salario: {self.salario}
Materia: {self.mater}\n\n""")

franco = Persona()

print("Inserire nome:")
nome = str(input("- "))

print("Inserire cognome:")
cognome = str(input("- "))

print("Inserire codice fiscale:")
cf = str(input("- "))

franco.assegna(nome, cognome, cf)
franco.mostra()


frank = Studente(franco.nome, franco.cognome, franco.codicefiscale)

frank.assegna_matricola('13425367543')
frank.assegna_universita('Politecnico')

giusto = Docente(franco.nome, franco.cognome, franco.codicefiscale)

giusto.assegna_salario('30')
giusto.assegna_materia('Italiano')

giusto.mostra()
