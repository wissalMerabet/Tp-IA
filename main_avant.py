from tkinter import *
from tkinter import ttk
from getInput import file, but, regles, baseFait
from chainageAvant import chainageAvant
from chainageAriere import chainageAriere

def action():
    f = entry.get()
    K, R, G = file(c=False, file=f)
    K, R, G = baseFait(K), regles(R), but(G)
    print(K)
    print(R)
    print(G)
    steps = chainageAvant(K, R ,G)
    update_table(steps)


def update_table(data):
    table.delete(*table.get_children())  #Efface les données existantes dans la table
    for i, step in enumerate(data, 1):
        cycle = f"Cycle {i}"
        base_de_fait = ','.join(step['base_de_fait'])
        regle_Applicable = step['regle_Applicable'] if step['regle_Applicable'] else "None"  # Récupère le contenu de la règle applicable ou affiche "None" s'il n'y en a pas
        table.insert("", "end", values=(cycle, base_de_fait, regle_Applicable))


root = Tk()
root.geometry("900x650")
root.title("Chainage avant")

label1 = Label(root, text=" Chainage Avant ")
entry = Entry(root)
label6 = Label(root, text="Entrer le nom du fichier : ")
btn1 = Button(root, text="Avant", command=action)

# Table
table = ttk.Treeview(root, columns=("cycle", "base_de_fait", "regle_Applicable"), show="headings")
table.heading("cycle", text="N° Cycle")
table.heading("base_de_fait", text="base_de_fait")
table.heading("regle_Applicable", text="regle_Applicable")


label1.place(x=350, y=10)
entry.place(x=350, y=45)
label6.place(x=100, y=45)
btn1.place(x=350, y=100)
table.place(x=50, y=150, width=800, height=400)

root.mainloop()
