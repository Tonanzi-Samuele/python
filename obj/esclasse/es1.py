class Rettangolo(object):
# attributi (privati)
    __base = 0.0
    __altezza = 0.0
# metodi (pubblici)
    def assegna(self, b, a):
        self.__base = b
        self.__altezza = a
    def area(self):
        return self.__base * self.__altezza
# funzione principale
def main():
    tovaglia = Rettangolo()
    tovaglia.assegna(5, 3)
    print("Area= ", tovaglia.area())
    tovaglia.__base = 10
    print("Area= ", tovaglia.area())
    # istruzione di avvio del programma
main()