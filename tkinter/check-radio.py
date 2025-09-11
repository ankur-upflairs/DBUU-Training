import tkinter as tk

root=tk.Tk()
root.geometry('600x400')
question=tk.Label(root,text='Choose your favourite subjects ?') 
question.pack()
pythonCheck=tk.BooleanVar()
javaCheck=tk.BooleanVar()
cPlusCheck=tk.BooleanVar()
def show_selection():
    print(f"python={pythonCheck.get()},java={javaCheck.get()},c++ ={cPlusCheck.get()}")
check1=tk.Checkbutton(root,text='python',variable=pythonCheck,
                      onvalue=True,offvalue=False)
check2=tk.Checkbutton(root,text='java',variable=javaCheck,
                      onvalue=True,offvalue=False)
check3=tk.Checkbutton(root,text='c++',variable=cPlusCheck,
                      onvalue=True,offvalue=False)
check1.pack()
check2.pack()
check3.pack()
button=tk.Button(root,text='click here',
                 command=show_selection)
button.pack()
question1=tk.Label(root,text='choose your gender ?')
question1.pack()
gender=tk.StringVar(value=None)
radio1=tk.Radiobutton(root,text='Male',variable=gender,value='male')
radio2=tk.Radiobutton(root,text='Female',variable=gender,value='female')
radio1.pack()
radio2.pack()

root.mainloop()
#pip install pillow 
