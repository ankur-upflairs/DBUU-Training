import tkinter as tk

root=tk.Tk()
root.title('my first window')
root.geometry('600x400')
# root.resizable(0,0)
label1=tk.Label(root,text='Hello world!!!' ,
                pady=20 ,bg='lightblue',fg='red',
                font=('Ariel',20))
label1.pack(side='left',fill='y')
def handle_click():
    print('button clicked!')
button1=tk.Button(root,text='Click Me!!!',
                  command=handle_click)
button1.pack(side='left' ,fill='both',expand=True)
button2=tk.Button(root,text='close window',
                  command=root.destroy)
button2.pack(side='left',fill='both',expand=True,
             padx=20,pady=20)
root.mainloop()
 