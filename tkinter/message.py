import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from PIL import Image,ImageTk

root=tk.Tk()
root.geometry('600x400')
root.title('Message box')
# msg1=messagebox.askokcancel(title='Choose One',message='please select yes for cancel')

def on_select1():
    messagebox.showerror('Error',"not allow")
def on_select2():
    # resp= messagebox.askokcancel('choose one','click ok for proceed')
    # resp= messagebox.askretrycancel('choose one','click retry for proceed')
    resp= messagebox.askyesnocancel('choose one','click ok for proceed')
    print(resp)
button1=tk.Button(root,text=f"button {1}",command=on_select1)
button1.pack(side='left')
button2=tk.Button(root,text=f"button {2}",command=on_select2)
button2.pack(side='left')
root.mainloop()


