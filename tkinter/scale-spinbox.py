import tkinter as tk
from PIL import Image,ImageTk
from tkinter import ttk

root=tk.Tk()
root.geometry('600x400')
root.title('Images App')
def on_move(event):
    print(scale1.get())
    print(scale.get())
scale=tk.Scale(root,from_=0,to=10,orient='horizontal',command=on_move)
scale.pack(pady=20)
scale1=ttk.Scale(root,from_=0,to=10,orient='horizontal',command=on_move)
scale1.pack()
def on_change():
    print(spin.get())
spin=ttk.Spinbox(root,from_=1,to=20,wrap=True ,increment=2,
                 values=(5,10,15,20),
                 command=on_change)
spin.pack(pady=10)
root.mainloop()
