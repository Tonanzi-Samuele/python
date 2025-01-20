#es 20 di pag 122
#Dato un elenco di n docenti con cognome e materia di insegnamento, 
#conta quanti sono i docenti di una materia prefissata 
#e fornita all'inizio. Organizza il programma con tre funzioni: una 
#per acquisire la materia da controllare, una per acquisire i dati e una per produrre il risultato.

import math



def acqusizione_dati(materia_rif):
    counter = 0
    while True:
        nom_ins = str(input("inserire nome insegnante: "))


