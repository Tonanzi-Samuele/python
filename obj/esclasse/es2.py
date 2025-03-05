class Auto():
    def __init__(self, marca,modello,prezzo):
        self.marca = marca
        self.modello = modello
        self.prezzo = prezzo
    def mostra(self):
        print(f"""\
        prezzo = {self.prezzo}
        modello = {self.modello}
        marca = {self.marca} """)


def main():
    panda = Auto("FIAT", "4x4", 20000)
    panda.mostra()
    

main()