import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import time
import os
import random
import json

class QuizPatente:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Patente B")
        self.root.geometry("800x600")
        self.root.configure(bg="#f0f0f0")
        self.root.resizable(False, False)
        
        # Variabili di stato
        self.domande = self.carica_domande()
        self.domanda_corrente = 0
        self.risposte_utente = [None] * len(self.domande)
        self.tempo_rimanente = 30 * 60  # 30 minuti in secondi
        self.quiz_iniziato = False
        self.quiz_terminato = False
        
        # Carica immagini
        self.immagini = {}
        self.carica_immagini()
        
        # Creazione dell'interfaccia
        self.crea_interfaccia()
        
    def carica_domande(self):
        # In un'applicazione reale, caricherei da un file JSON o database
        domande = [
            {
                "testo": "Il segnale di STOP impone l'arresto e la concessione di precedenza a tutti i veicoli",
                "immagine": "stop.png",
                "risposta_corretta": True
            },
            {
                "testo": "Il limite di velocità nei centri abitati è generalmente di 70 km/h",
                "immagine": "limite_velocita.png",
                "risposta_corretta": False
            },
            {
                "testo": "È consentito sorpassare in prossimità di un dosso",
                "immagine": "dosso.png",
                "risposta_corretta": False
            },
            {
                "testo": "Il segnale di pericolo generico preannuncia un pericolo diverso da quelli previsti dagli altri segnali",
                "immagine": "pericolo_generico.png",
                "risposta_corretta": True
            },
            {
                "testo": "La striscia longitudinale continua consente il sorpasso se non ci sono veicoli dalla direzione opposta",
                "immagine": "striscia_continua.png",
                "risposta_corretta": False
            },
            {
                "testo": "È obbligatorio allacciare le cinture di sicurezza anche nei sedili posteriori",
                "immagine": "cinture.png",
                "risposta_corretta": True
            },
            {
                "testo": "Il segnale di diritto di precedenza indica che si ha la precedenza sugli altri veicoli agli incroci",
                "immagine": "precedenza.png",
                "risposta_corretta": True
            },
            {
                "testo": "La patente B consente di guidare motocicli di qualsiasi cilindrata",
                "immagine": "patente.png",
                "risposta_corretta": False
            },
            {
                "testo": "Il tasso alcolemico consentito per i neopatentati è pari a zero",
                "immagine": "alcol.png",
                "risposta_corretta": True
            },
            {
                "testo": "Il triangolo di emergenza va posizionato a non meno di 50 metri dal veicolo in panne",
                "immagine": "triangolo.png",
                "risposta_corretta": True
            }
        ]
        return domande
    
    def carica_immagini(self):
        # In un'applicazione reale, le immagini andrebbero nella stessa cartella del programma
        # Per questa simulazione, generiamo un'immagine di esempio per ogni segnale
        for domanda in self.domande:
            nome_file = domanda["immagine"]
            # Usiamo un Canvas per creare un'immagine di esempio
            img_canvas = tk.Canvas(width=200, height=200)
            img_canvas.create_rectangle(20, 20, 180, 180, fill="#ffffff", outline="#000000")
            
            if "stop" in nome_file:
                img_canvas.create_polygon(100, 20, 180, 100, 100, 180, 20, 100, fill="red")
                img_canvas.create_text(100, 100, text="STOP", fill="white", font=("Arial", 16, "bold"))
            elif "limite" in nome_file:
                img_canvas.create_oval(30, 30, 170, 170, fill="white", outline="red", width=10)
                img_canvas.create_text(100, 100, text="50", fill="black", font=("Arial", 40, "bold"))
            elif "dosso" in nome_file:
                img_canvas.create_polygon(20, 140, 60, 60, 100, 140, 140, 60, 180, 140, fill="yellow", outline="black")
                img_canvas.create_text(100, 100, text="!", fill="black", font=("Arial", 40, "bold"))
            elif "pericolo" in nome_file:
                img_canvas.create_polygon(100, 30, 170, 150, 30, 150, fill="yellow", outline="black")
                img_canvas.create_text(100, 100, text="!", fill="black", font=("Arial", 40, "bold"))
            elif "striscia" in nome_file:
                img_canvas.create_rectangle(20, 80, 180, 120, fill="grey")
                img_canvas.create_line(100, 30, 100, 170, fill="white", width=5)
            elif "cinture" in nome_file:
                img_canvas.create_oval(50, 40, 150, 100, fill="blue")
                img_canvas.create_rectangle(60, 90, 140, 160, fill="blue")
                img_canvas.create_line(70, 70, 130, 130, fill="white", width=5)
                img_canvas.create_line(130, 70, 70, 130, fill="white", width=5)
            elif "precedenza" in nome_file:
                img_canvas.create_polygon(20, 100, 100, 20, 180, 100, 100, 180, fill="yellow", outline="black")
            elif "patente" in nome_file:
                img_canvas.create_rectangle(40, 40, 160, 160, fill="pink")
                img_canvas.create_text(100, 100, text="B", fill="black", font=("Arial", 60, "bold"))
            elif "alcol" in nome_file:
                img_canvas.create_oval(60, 40, 140, 100, fill="red")
                img_canvas.create_rectangle(80, 100, 120, 160, fill="red")
                img_canvas.create_line(50, 50, 150, 150, fill="white", width=5)
            elif "triangolo" in nome_file:
                img_canvas.create_polygon(100, 30, 170, 150, 30, 150, fill="red", outline="red")
                img_canvas.create_polygon(100, 50, 150, 130, 50, 130, fill="white")
            
            # Converti il canvas in immagine
            self.immagini[nome_file] = ImageTk.PhotoImage(img_canvas.postscript(colormode="color"))
    
    def crea_interfaccia(self):
        # Frame superiore per titolo e timer
        self.frame_superiore = tk.Frame(self.root, bg="#4a7abc", height=60)
        self.frame_superiore.pack(fill=tk.X)
        
        self.label_titolo = tk.Label(self.frame_superiore, text="Quiz Patente B", 
                                   font=("Arial", 20, "bold"), bg="#4a7abc", fg="white")
        self.label_titolo.pack(side=tk.LEFT, padx=20, pady=10)
        
        self.frame_timer = tk.Frame(self.frame_superiore, bg="#4a7abc")
        self.frame_timer.pack(side=tk.RIGHT, padx=20, pady=10)
        
        self.label_timer = tk.Label(self.frame_timer, text="Tempo: 30:00", 
                                   font=("Arial", 14), bg="#4a7abc", fg="white")
        self.label_timer.pack(side=tk.RIGHT)
        
        # Frame principale
        self.frame_principale = tk.Frame(self.root, bg="#f0f0f0")
        self.frame_principale.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Frame di benvenuto
        self.frame_benvenuto = tk.Frame(self.frame_principale, bg="#f0f0f0")
        self.frame_benvenuto.pack(fill=tk.BOTH, expand=True)
        
        tk.Label(self.frame_benvenuto, text="Benvenuto al Quiz della Patente B", 
               font=("Arial", 22, "bold"), bg="#f0f0f0").pack(pady=40)
        
        tk.Label(self.frame_benvenuto, text="Istruzioni:", 
               font=("Arial", 14, "bold"), bg="#f0f0f0").pack(anchor=tk.W, padx=40, pady=(20, 10))
        
        istruzioni = """
        • Il quiz è composto da 10 domande con risposta VERO o FALSO
        • Hai 30 minuti di tempo per completare il quiz
        • Puoi navigare liberamente tra le domande
        • Per superare il test devi rispondere correttamente ad almeno 8 domande
        """
        
        tk.Label(self.frame_benvenuto, text=istruzioni, 
               font=("Arial", 12), bg="#f0f0f0", justify=tk.LEFT).pack(anchor=tk.W, padx=60)
        
        self.btn_inizia = tk.Button(self.frame_benvenuto, text="Inizia Quiz", 
                                  font=("Arial", 14, "bold"), bg="#4a7abc", fg="white",
                                  width=20, height=2, command=self.inizia_quiz)
        self.btn_inizia.pack(pady=40)
        
        # Frame del quiz (inizialmente nascosto)
        self.frame_quiz = tk.Frame(self.frame_principale, bg="#f0f0f0")
        
        # Barra di avanzamento tempo
        self.frame_progresso = tk.Frame(self.frame_quiz, bg="#f0f0f0")
        self.frame_progresso.pack(fill=tk.X, pady=(0, 20))
        
        self.progress_var = tk.DoubleVar()
        self.barra_progresso = ttk.Progressbar(self.frame_progresso, variable=self.progress_var, 
                                             length=760, mode="determinate")
        self.barra_progresso.pack(fill=tk.X)
        
        # Frame domanda
        self.frame_domanda = tk.Frame(self.frame_quiz, bg="white", bd=1, relief=tk.SOLID)
        self.frame_domanda.pack(fill=tk.BOTH, expand=True, pady=10)
        
        # Numero domanda
        self.label_num_domanda = tk.Label(self.frame_domanda, text="Domanda 1/10", 
                                        font=("Arial", 12, "bold"), bg="white")
        self.label_num_domanda.pack(anchor=tk.W, padx=20, pady=10)
        
        # Testo domanda
        self.label_testo_domanda = tk.Label(self.frame_domanda, text="", 
                                         font=("Arial", 14), bg="white", wraplength=700, justify=tk.LEFT)
        self.label_testo_domanda.pack(padx=20, pady=10, anchor=tk.W)
        
        # Frame immagine
        self.frame_immagine = tk.Frame(self.frame_domanda, bg="white")
        self.frame_immagine.pack(pady=10)
        
        self.label_immagine = tk.Label(self.frame_immagine, bg="white")
        self.label_immagine.pack()
        
        # Frame risposta
        self.frame_risposta = tk.Frame(self.frame_domanda, bg="white")
        self.frame_risposta.pack(pady=20)
        
        self.var_risposta = tk.BooleanVar()
        
        self.rb_vero = tk.Radiobutton(self.frame_risposta, text="VERO", variable=self.var_risposta, 
                                    value=True, font=("Arial", 12), bg="white",
                                    command=self.registra_risposta)
        self.rb_vero.pack(side=tk.LEFT, padx=20)
        
        self.rb_falso = tk.Radiobutton(self.frame_risposta, text="FALSO", variable=self.var_risposta, 
                                     value=False, font=("Arial", 12), bg="white",
                                     command=self.registra_risposta)
        self.rb_falso.pack(side=tk.LEFT, padx=20)
        
        # Frame navigazione
        self.frame_navigazione = tk.Frame(self.frame_quiz, bg="#f0f0f0")
        self.frame_navigazione.pack(fill=tk.X, pady=10)
        
        self.btn_precedente = tk.Button(self.frame_navigazione, text="◀ Precedente", 
                                      font=("Arial", 12), command=self.domanda_precedente)
        self.btn_precedente.pack(side=tk.LEFT)
        
        self.btn_successiva = tk.Button(self.frame_navigazione, text="Successiva ▶", 
                                      font=("Arial", 12), command=self.domanda_successiva)
        self.btn_successiva.pack(side=tk.RIGHT)
        
        # Frame pulsanti domande
        self.frame_pulsanti_domande = tk.Frame(self.frame_quiz, bg="#f0f0f0")
        self.frame_pulsanti_domande.pack(fill=tk.X, pady=10)
        
        self.pulsanti_domande = []
        for i in range(len(self.domande)):
            btn = tk.Button(self.frame_pulsanti_domande, text=str(i+1), width=3, height=1,
                          command=lambda idx=i: self.vai_a_domanda(idx))
            btn.pack(side=tk.LEFT, padx=5)
            self.pulsanti_domande.append(btn)
        
        # Pulsante invio quiz
        self.btn_invio = tk.Button(self.frame_quiz, text="Termina e Invia Quiz", 
                                 font=("Arial", 12, "bold"), bg="#4a7abc", fg="white",
                                 command=self.termina_quiz)
        self.btn_invio.pack(pady=20)
        
    def inizia_quiz(self):
        self.quiz_iniziato = True
        self.frame_benvenuto.pack_forget()
        