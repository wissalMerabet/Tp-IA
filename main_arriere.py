from tkinter import *
from tkinter import ttk
from getInput import file, but, regles, baseFait
from chainageAriere import chainageAriere


def action1():
    #Récupère les données
    f = entry.get()
    K, R, G = file(c=False, file=f)
    K, R, G = baseFait(K), regles(R), but(G)
    output = chainageAriere(G, K, R)
    print(output)
    formatted_output = ""
    for step in output:
        out = step[0]
        #print(step[1])
        applicable_rule = ""
        if len(step) > 1 and step[1] is not None:
            applicable_rule = f" - Aplicable Rule: {step[1]}" # si pas de regles
        formatted_output += f"{out}{applicable_rule}\n"

    label4.config(text=formatted_output)
    #print(formatted_output)
    label4.update()


root = Tk()
root.geometry("800x1000")
root.title("Chainage avant")

label1 = Label(root, text=" Chainage Ariere ")
entry = Entry(root)
label6 = Label(root,text="Entrer le nom du fichier : ")
btn1 = Button(root, text="Ariere",command=action1)
label4 = Label(root, text="" , bg='white')

label1.place(x=350, y=10)
entry.place(x=350, y=45)
label6.place(x=100, y=45)
label4.place(x=330, y=150)
btn1.place(x=350, y=100)

root.mainloop()