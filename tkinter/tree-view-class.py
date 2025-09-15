import tkinter as tk
from tkinter import ttk
from PIL import Image,ImageTk

root=tk.Tk()
root.geometry('600x400')
root.title('Images App')
root.columnconfigure(0,weight=1)
root.rowconfigure(0,weight=1)

tree=ttk.Treeview(root)
tree["columns"]=("name",'age')
tree.column('#0',width=0,minwidth=0,stretch=False)
tree.column('name',width=80,minwidth=50,anchor=tk.CENTER)
tree.column('age',width=80,minwidth=50,anchor=tk.CENTER)
tree.heading('name',text="Name")
tree.heading('age',text="Age")
tree.grid(sticky='nswe',padx=5,pady=5)
tree.insert(parent='',index="end",iid=0,
            values=('Sunil',23))
tree.insert(parent='',index="end",iid=1,
            values=('Pawan',25))
root.mainloop()
