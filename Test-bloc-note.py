from tkinter import *
from tkinter.filedialog import *
import tkinter as tk

# new windows
window = Tk()

# variable d windows
window.title("Bloc-note")
window.geometry("700x600")
window.minsize(699, 599)

# cree un menu bar
menubar = Menu(window)

menu1 = Menu(menubar, tearoff=0)
menu1.add_command(label="New")
menu1.add_command(label="Save")
menu1.add_command(label="Open")
menu1.add_command(label="Edit")
menu1.add_separator()
menu1.add_command(label="Quit")
menubar.add_cascade(label="File", menu=menu1)

menu2 = Menu(menubar, tearoff=0)
menu2.add_command(label="A propos")
menubar.add_cascade(label="Help", menu=menu2)

# zone d'entrer de text
text1 = tk.Text(window, height=100, width=100)
text1.pack()

window.config(menu=menubar)

# cree la boucle
window.mainloop()