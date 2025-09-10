import tkinter as tk

root=tk.Tk()
root.title('my first window')
root.geometry('600x400')
# root.resizable(0,0)
frame1=tk.Frame(root)
frame1.pack(expand=True)
frame2=tk.Frame(root)
frame2.pack(expand=True)
label1=tk.Label(frame1,text='Hello world!!!' ,
                pady=20 ,bg='lightblue',fg='red',
                font=('Ariel',20))
label1.pack(side='left',fill='both')
label2=tk.Label(frame1,text='Hello world!!!' ,
                pady=20 ,bg='black',fg='red',
                font=('Ariel',20))
label2.pack(side='left',fill='both')
label3=tk.Label(frame2,text='Hello world!!!' ,
                pady=20 ,bg='green',fg='red',
                font=('Ariel',20))
label3.pack(side='left',fill='both')
label4=tk.Label(frame2,text='Hello world!!!' ,
                pady=20 ,bg='yellow',fg='red',
                font=('Ariel',20))
label4.pack(side='left',fill='both')

root.mainloop()
 