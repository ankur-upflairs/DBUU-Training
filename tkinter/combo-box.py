import tkinter as tk
from tkinter import ttk
from PIL import Image,ImageTk
tech=['Html','css','javascript','react']
root=tk.Tk()
root.geometry('600x400')
root.title('Images App')
combo_var= tk.StringVar()
def on_select(e):
    print(dropdown.get(),combo_var.get())
    # dropdown.current(3)
def on_drop():
    print('hello')
dropdown= ttk.Combobox(root,values=tech,width=30,
                       textvariable=combo_var,
                       postcommand=on_drop)
dropdown.pack()
dropdown.bind('<<ComboboxSelected>>',on_select)
root.mainloop()
