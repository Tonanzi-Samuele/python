import tkinter as tk
from tkinter import messagebox, ttk
import time

class QuizPatente:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Patente B")
        self.root.geometry("800x600")

        self.questions = [
            {"question": "Il segnale raffigurato indica una strada senza uscita.", "answer": True, "image": "segnale1.png"},
            {"question": "È obbligatorio dare la precedenza ai pedoni sulle strisce.", "answer": True, "image": "segnale2.png"},
            {"question": "Un veicolo può superare i 50 km/h nei centri abitati.", "answer": False, "image": "segnale3.png"}
        ]
        self.current_question = 0
        self.answers = [None] * len(self.questions)
        self.start_time = time.time()
        self.max_time = 30 * 60  # 30 minuti
        
        self.create_widgets()
        self.update_timer()
        self.load_question()
    
    def create_widgets(self):
        self.label_question = tk.Label(self.root, text="", wraplength=600, font=("Arial", 14))
        self.label_question.pack(pady=20)
        
        self.canvas = tk.Canvas(self.root, width=200, height=200)
        self.canvas.pack()
        
        self.var_answer = tk.BooleanVar()
        self.radio_true = tk.Radiobutton(self.root, text="Vero", variable=self.var_answer, value=True)
        self.radio_false = tk.Radiobutton(self.root, text="Falso", variable=self.var_answer, value=False)
        self.radio_true.pack()
        self.radio_false.pack()
        
        self.button_prev = tk.Button(self.root, text="Precedente", command=self.prev_question)
        self.button_next = tk.Button(self.root, text="Successiva", command=self.next_question)
        self.button_submit = tk.Button(self.root, text="Invia Risposte", command=self.submit_quiz)
        
        self.button_prev.pack(side=tk.LEFT, padx=20, pady=20)
        self.button_next.pack(side=tk.LEFT, padx=20, pady=20)
        self.button_submit.pack(side=tk.RIGHT, padx=20, pady=20)
        
        self.progress = ttk.Progressbar(self.root, orient=tk.HORIZONTAL, length=600, mode='determinate')
        self.progress.pack(pady=10)
    
    def load_question(self):
        q = self.questions[self.current_question]
        self.label_question.config(text=q["question"])
        
        if self.answers[self.current_question] is not None:
            self.var_answer.set(self.answers[self.current_question])
        else:
            self.var_answer.set(False)  # Oppure True, ma meglio False come default
    
    def next_question(self):
        self.answers[self.current_question] = self.var_answer.get()
        if self.current_question < len(self.questions) - 1:
            self.current_question += 1
            self.load_question()
    
    def prev_question(self):
        self.answers[self.current_question] = self.var_answer.get()
        if self.current_question > 0:
            self.current_question -= 1
            self.load_question()
    
    def submit_quiz(self):
        self.answers[self.current_question] = self.var_answer.get()
        score = sum([self.answers[i] == q["answer"] for i, q in enumerate(self.questions)])
        messagebox.showinfo("Risultato", f"Punteggio finale: {score}/{len(self.questions)}")
        self.root.quit()
    
    def update_timer(self):
        elapsed = time.time() - self.start_time
        remaining = self.max_time - elapsed
        if remaining <= 0:
            self.submit_quiz()
            return
        self.progress["value"] = (elapsed / self.max_time) * 100
        self.root.after(1000, self.update_timer)

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizPatente(root)
    root.mainloop()
