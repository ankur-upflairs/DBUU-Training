import tkinter as tk

user_details={
    'userName':'abc',
    'password':"123"
}

root=tk.Tk()
root.title('Login form')
root.geometry('600x400')

name_value=tk.StringVar()
pass_value=tk.StringVar()


def print_value():
    # print(entry.get())
    # print(name_value.get())
    # print(pass_value.get())
    if(user_details['userName']==name_value.get()):
        if user_details['password']==pass_value.get():
            print('user is authenticated')
        else:
            print('password does not matcch')
    else:
        print('user not found')
    result_label['text']=name_value.get()
    name_value.set('')
    pass_value.set('')
nameFrame=tk.Frame(root)
nameFrame.pack()
label=tk.Label(nameFrame,text='Enter Your UserName : ')
label.pack(side="left",pady=10)

entry=tk.Entry(nameFrame,textvariable=name_value,)
entry.pack(side="left",pady=10)
passwordFrame=tk.Frame(root)
passwordFrame.pack()
label2=tk.Label(passwordFrame,text='Enter Your Password : ')
label2.pack(side="left",pady=10)

entry2=tk.Entry(passwordFrame,textvariable=pass_value,show='*')
entry2.pack(side="left",pady=10)

button=tk.Button(root,text='Click Here...',
                 command=print_value)
# button['state']='disabled'
button.pack()

result_label=tk.Label(root)
result_label.pack()
root.mainloop()