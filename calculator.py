import tkinter as tk

def calculatrice():
    # Fonction pour effectuer le calcul
    def calculer():
        expression = entry.get()
        try:
            resultat = eval(expression)
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(resultat))
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Erreur")

    # Fonction pour ajouter un caractère à l'entrée
    def ajouter_caractere(caractere):
        current = entry.get()
        entry.delete(0, tk.END)
        entry.insert(tk.END, current + caractere)

    # Fonction pour effacer l'entrée
    def effacer():
        entry.delete(0, tk.END)

    # Configuration de la fenêtre principale
    fenetre = tk.Tk()
    fenetre.title("Calculatrice")

    # Entrée pour afficher l'expression
    entry = tk.Entry(fenetre, width=20, font=("Arial", 16), justify="right")
    entry.grid(row=0, column=0, columnspan=4)

    # Boutons pour les chiffres
    chiffres = "7894561230"
    row_val = 1
    col_val = 0
    for chiffre in chiffres:
        tk.Button(fenetre, text=chiffre, width=5, height=2, command=lambda c=chiffre: ajouter_caractere(c)).grid(row=row_val, column=col_val)
        col_val += 1
        if col_val > 2:
            col_val = 0
            row_val += 1

    # Boutons pour les opérations
    operations = "+-*/"
    row_op = 1
    col_op = 3
    for operation in operations:
        tk.Button(fenetre, text=operation, width=5, height=2, command=lambda o=operation: ajouter_caractere(o)).grid(row=row_op, column=col_op)
        row_op += 1

    # Bouton égal
    tk.Button(fenetre, text="=", width=5, height=2, command=calculer).grid(row=4, column=2)

    # Bouton effacer
    tk.Button(fenetre, text="C", width=5, height=2, command=effacer).grid(row=4, column=0)

    # Exécution de la boucle principale de la fenêtre
    fenetre.mainloop()

# Appel de la fonction pour afficher la calculatrice
calculatrice()
