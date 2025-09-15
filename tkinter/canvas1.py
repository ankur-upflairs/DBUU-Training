import tkinter as tk


root=tk.Tk()
root.geometry('400x350')
def on_move():
    rect=canvas.find_withtag('rect')
    x1,y1,x2,y2=canvas.coords(rect)
    canvas.coords(rect,x1+20,y1,x2+20,y2)
    # print(canvas.coords(rect))

canvas=tk.Canvas(root,width=400,height=300,background='black')
canvas.pack()
canvas.create_text(300,40,text='Hello Everyone!',fill='white',font=('Ariel',20))
canvas.create_line(0,0,400,300,fill='white')
canvas.create_line(20,30,40,50,100,0,300,0,fill='green',width=3)
canvas.create_rectangle(20,20,100,100,fill='yellow',tags='rect')
canvas.create_oval(20,20,100,150,fill='tan')
canvas.create_polygon(100,180,200,180,130,220,fill='white')
button=tk.Button(root,text='move right',command=on_move)
button.pack()
root.mainloop()

