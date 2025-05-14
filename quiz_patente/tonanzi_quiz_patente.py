import tkinter as tk
from PIL import Image,ImageTk
import modulo_domande as md
import random
from tkinter import messagebox
FILE = "ao.json"

class finestra1(tk.Frame):
    def __init__(self, master = None):
        super().__init__(master)
        self.crea_home()
    def crea_home(self):
        self.LabelTitolo = tk.Label(self.master, text = "QUIZ PATENTE",
                                    background= "lightgreen",
                                    foreground= "darkgreen",
                                    font= ("Arial", 40, "bold italic"),
                                    padx=20, pady=10,
                                    relief="ridge", borderwidth=3)
        self.LabelTitolo.pack(pady = 30)
        self.button = tk.Button(self.master, text = "inizia", command=main2,bg = "green",foreground="white", font=("Arial",40, "bold"))
        self.button.place(x = 600, y = 320)
        
        
class finestra2(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.idDomanda = 0
        self.errori = 0
        self.current = 0
        self.array = []
        self.array_risposte = []  
        self.arrayimg = []
        self.domanda = ""
        self.risposta = ""
        self.minuti = 30
        self.secondi = self.minuti * 60
        self.punti = 0  
        self.risposte_date = {}  
        self.id = 0
        self.crea_finestra()
        
        
    def leggi_domanda(self):
        for self.id in range(0, 30):
            self.idDomanda = random.randint(0, len(md.domande)-1) 
            self.domanda = md.domande[self.idDomanda]["domanda"]
            self.risposta = md.domande[self.idDomanda]["risposta"]
            self.img = md.domande[self.idDomanda]["immagine"]
            self.arrayimg.append(self.img) 
            self.array.append(self.domanda) #domanda
            self.array_risposte.append(self.risposta) #risposta
        print(self.array)
        print(len(md.domande))
    
    def prendi_immagine(self):
            img = Image.open(self.arrayimg[self.current])
            self.immagine = ImageTk.PhotoImage(img)
            self.label_img.config(image=self.immagine)
    
    def crea_finestra(self):
        print(self.current)
        self.leggi_domanda()
        

        self.LabelTitolo = tk.Label(self, text = "QUIZ PATENTE",
                                    background= "lightgreen",
                                    foreground= "darkgreen",
                                    font= ("Arial", 40, "bold italic"),
                                    padx=20, pady=10,
                                    relief="ridge", borderwidth=3)
        self.LabelTitolo.pack(pady = 20)
        
        
        self.label_numero_domanda = tk.Label(self, text=f"Domanda: {self.current + 1}/{len(self.array)}",
                                   fg="black", bg="orange", 
                                   font=("Arial", 15, "bold"))
        self.label_numero_domanda.place(x=100, y=27)
        
        self.label_img = tk.Label(self,
                                 bg="white")
        self.label_img.place(x = 600, y = 150)
        self.label_domanda = tk.Label(self, 
                                    text = self.array[self.current],
                                     fg = "black", bg= "orange", font = ("Arial", 16,"bold"),wraplength="500")
        self.label_domanda.pack(pady = 250)
        
        
        self.button1 = tk.Button(self, text = "Vero", 
                                command=self.risposta_vero,
                                bg = "green",
                                foreground="white", 
                                font=("Arial",15, "bold"))
        self.button1.place(x = 500, y = 500)
        
        self.button2 = tk.Button(self, text = "Falso",
                                command=self.risposta_falso,
                                bg = "red",
                                foreground="white", 
                                font=("Arial",15, "bold"))
        self.button2.place(x = 790, y = 500)
        
        self.button3 = tk.Button(self, text = "Indietro",
                                 command = self.indietro,
                                bg = "grey",
                                foreground="white", 
                                font=("Arial",15, "bold"))
        self.button3.place(x = 500, y = 600)
        
        self.button4 = tk.Button(self, text = "Avanti",
                                 command = self.avanti,
                                bg = "grey",
                                foreground="white", 
                                font=("Arial",15, "bold"))
        self.button4.place(x = 790, y = 600)

        
        self.buttoncons = tk.Button(self, text = "CONSEGNA",
                                 command = self.consegna,
                                bg = "blue",
                                foreground="white", 
                                font=("Arial",20, "bold"))
        self.buttoncons.place(x = 100, y = 70)
        
        self.label_timer = tk.Label(self, text='00:00', bg="orange", font=("Arial", 15, "bold"))
        self.label_timer.place(x = 1100, y =27)
        self.start_timer()
        self.prendi_immagine()


        
    def risposta_vero(self):
        
        self.risposte_date[self.current] = "True"
        
        
        if self.array_risposte[self.current] == "True":
            self.punti += 1
        else:
            self.errori +=1
        
        
        self.avanti()
        
    def risposta_falso(self):
        
        self.risposte_date[self.current] = "False"
        
        
        if self.array_risposte[self.current] == "False":
            self.punti += 1
        else:
            self.errori +=1
        
        
        self.avanti()
    
    def start_timer(self):
        if self.secondi > 0:
            self.min_restanti = self.secondi // 60
            self.sec_restanti = self.secondi % 60
            self.label_timer.config(text=f'{self.min_restanti:02d}:{self.sec_restanti:02d}')
            self.secondi -= 1
            self.after(1000, self.start_timer)
        else:
            messagebox.showinfo("TEMPO SCADUTO", "Test consegnato!", parent = self)
            self.consegna()

    def consegna(self):
        
        domande_risposte = len(self.risposte_date)
        
        
        if domande_risposte == 0:
            messagebox.showinfo("Quiz Non Completato", "Non hai risposto a nessuna domanda!", parent=self)
        else:
            
            esito = "SUPERATO" if self.punti >= 27 else "NON SUPERATO"
            
            
            messagebox.showinfo("Risultato Quiz", 
                               f"Test completato!\n\n"
                               f"Risposte corrette: {self.punti} su 30\n"
                               f"Esito: {esito}", 
                               parent=self)
        
        
        self.destroy()
    
    def avanti(self):
        if self.current == len(self.array) - 1:
            messagebox.showinfo(title = "Fine Quiz", message="Hai raggiunto l'ultima domanda. Premi 'CONSEGNA' per vedere il risultato.", parent=self)
        else: 
            self.current+= 1
            self.label_domanda.config(text = self.array[self.current])
            self.prendi_immagine()
            self.label_numero_domanda.config(text=f"Domanda: {self.current + 1}/{len(self.array)}")
    
    def indietro(self):
        if self.current == 0:
            messagebox.showerror(title = "ERRORE", message="Sei alla prima domanda", parent=self)
        else:
            self.current -= 1
            self.label_domanda.config(text = self.array[self.current])
            self.prendi_immagine()
            self.label_numero_domanda.config(text=f"Domanda: {self.current + 1}/{len(self.array)}")
    
def main2():
    window2 = finestra2()
    window2.geometry("1440x1080")
    window2.configure(bg = "lightgreen") 
    window2.resizable(0,0)
    window2.mainloop()

def main():
    window = finestra1()
    window.master.geometry("1440x1080")
    window.master.configure(bg = "lightgreen") 
    window.master.resizable(0,0)
    window.mainloop()

main()