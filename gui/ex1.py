# finestra.py: contenitore grafico con etichetta e pulsante
import tkinter as tk #libreria tkinter (con l'alias tk), che è una libreria per creare interfacce grafiche utente (GUI) in Python

#tk.Frame è una classe di Tkinter che rappresenta una "finestra" o una "sezione" 
# all'interno della finestra principale, un contenitore per i widget (come pulsanti, etichette, etc.). 
# Usare un Frame è un buon modo per organizzare e gestire i widget.
  
class Finestra(tk.Frame):
# costruttore 
    def __init__(self, master = None):
        #Il parametro master rappresenta la finestra principale (di solito, un oggetto Tk()), 
        # e se non viene fornito, il valore di default sarà None.
        super().__init__(master)        
        self.master.title("Finestra grafica di default")        
        self.master.geometry("300x200")        
        self.grid()        
        self.crea_widgets()
    # inserimento dei widget
    def crea_widgets(self):
        self.lbl1 = tk.Label(self, text = "Inserisci il tuo nome ")
        self.lbl1.grid(row = 0, column = 0)
        self.btn1 = tk.Button(self, text = "Avanti")
        self.btn1.grid(row = 0, column = 1)

def main():
    f = Finestra()    
    f.master.title("Finestra grafica")    
    f.master.geometry("900x600")    
    f.master.resizable(0,0)   #non si può ridimensionare la finestra
    f.mainloop() # #Avvia il ciclo principale dell'interfaccia grafica. 
#Senza questo, la finestra si chiuderebbe subito dopo essere stata aperta

main()