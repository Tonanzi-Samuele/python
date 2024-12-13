def aggiungi():
#    prestito = {
#        "nome": "",
#        "titolo":"",
#        "data": ""
#    }
#    for i
#    nome = str(input("inserire nome:"))
#    titolo = str(input("inserire titolo: "))
#    data = str(input("inserire data: "))
#    prestito["nome"] = nome
#    prestito["titolo"] = titolo
#    prestito["data"] = data
#    print(prestito)
    prestito = []
    prestiti = []
    for i in range(5):
        nome = str(input("Inserire nome e cognome: "))
        titolo = str(input("inserire titolo: "))
        data = str(input("inserire data: "))
        prestito.append(nome)
        prestito.append(titolo)
        prestito.append(data)
        prestiti.append(prestito)
        prestito = []
    print(prestiti)

def main():
    aggiungi()
main()