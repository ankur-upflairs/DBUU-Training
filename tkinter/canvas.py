import tkinter as tk 
from PIL import Image,ImageTk 

root=tk.Tk()
root.geometry('600x400')
root.title('Canvas')
canvas=tk.Canvas(root,width=500,height=400,bg='white')
canvas.create_line(0,100,100,50,30,10,width=2,fill='green')
canvas.create_rectangle(10,10,100,100)
canvas.create_oval(200,200,400,400,fill='tan',outline='green')
canvas.pack()

root.mainloop()






