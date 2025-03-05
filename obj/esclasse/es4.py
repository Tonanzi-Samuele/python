class Utente():
    def __init__(self, __nome = "", __password = ""):
        
        self.__nome = __nome
        self.__password = __password

    def agg(self,__nome, __password):
        self.__nome = __nome
        
        if len(__password) >= 8:
            self.__password = __password
        else:
            self.password = ""

    def stampa(self):
        if self.__password == "":
            print("password non valida1")
        else:
            print("password valida")


Trilli = Utente()
edo = Utente()
andrew = Utente()

Trilli = ("subnettatore")
edo.agg("ricky", "oneoneone")
edo.stampa()

