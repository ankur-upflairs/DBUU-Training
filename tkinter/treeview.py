import tkinter as tk
from tkinter import ttk
data = [
    ("Sunil", 25),
    ("Pawan", 30),
    ("Ankur", 27),
    ("Ravi", 22),
    ("Priya", 29),
    ("Meena", 35),
    ("Arjun", 28),
    ("Kiran", 32),
    ("Sita", 24),
    ("Rahul", 26)
]
def on_select(event):
    print(tree.selection())
root=tk.Tk()
root.geometry('600x400')
tree= ttk.Treeview(root,selectmode='browse')
tree['columns']= ('Name','Age')
tree.column('#0',minwidth=0,width=0,anchor='w',stretch=tk.NO)
tree.column('Name',minwidth=50,anchor=tk.CENTER)
tree.column('Age',minwidth=50,anchor='center')
tree.heading('Name',text="Name")
tree.heading('Age',text='Age')
# tree.insert(parent='',text="",index='end',iid=0,values=("sunil","pawan"))
for i,s in enumerate(data):
    tree.insert(parent='',text="",index='end',iid=i,values=s)
tree.bind('<<TreeviewSelect>>',on_select)
tree.grid(row=0,column=0,sticky='nswe')
root.mainloop()
