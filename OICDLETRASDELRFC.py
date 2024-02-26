import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import networkx as nx

class AutomataRFC:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Validación de RFC")

        self.entry_label = tk.Label(self.root, text="Ingrese la cadena RFC:")
        self.entry_label.pack()

        self.entry = tk.Entry(self.root)
        self.entry.pack()

        self.result_label = tk.Label(self.root, text="")
        self.result_label.pack()

        self.validate_button = tk.Button(self.root, text="Validar", command=self.validar_rfc_and_show)
        self.validate_button.pack()

    def validar_rfc_and_show(self):
        rfc = self.entry.get().upper()  
        
        # Verificar si la primera letra es 'O'
        if rfc[0] != 'O':
            self.result_label.config(text="Cadena RFC no válida. El estado inicial debe ser 'O'.")
            return
        
        # Verificar que la cadena contenga solo las letras 'O', 'I', 'C', 'D' y no más de 4 letras en total
        if any(letra not in ['O', 'I', 'C', 'D'] for letra in rfc) or len(rfc) > 4:
            self.result_label.config(text="Cadena RFC no válida. La cadena debe contener solo las letras 'O', 'I', 'C', 'D' y tener como máximo 4 caracteres.")
            return

        self.result_label.config(text="Cadena RFC válida.")

        self.mostrar_automata()

    def mostrar_automata(self):
        rfc = self.entry.get().upper()  # Obtener la cadena RFC ingresada

        
        for widget in self.root.winfo_children():
            if isinstance(widget, tk.Canvas):
                widget.destroy()

    
        G = nx.DiGraph()

        
        for letra in rfc:
            G.add_node(letra)

        
        for i in range(len(rfc) - 1):
            G.add_edge(rfc[i], rfc[i+1])

       
        fig, ax = plt.subplots(figsize=(6, 4))
        pos = nx.spring_layout(G, seed=42)  

        
        nx.draw(G, pos, with_labels=True, node_size=2000, node_color='lightblue', font_size=16, arrows=True, ax=ax)

        
        canvas = FigureCanvasTkAgg(fig, master=self.root)
        canvas.draw()
        canvas.get_tk_widget().pack()



    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    automata = AutomataRFC()
    automata.run()
