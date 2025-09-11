import tkinter as tk

user_details={
    'userName':'abc',
    'password':"123"
}

root=tk.Tk()
root.title('Login form')
root.geometry('600x400')
root.columnconfigure(0,weight=1)
root.columnconfigure(1,weight=1)

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

label=tk.Label(root,text='Enter Your UserName : ')
label.grid(row=0,column=0,padx=30,pady=10)

entry=tk.Entry(root,textvariable=name_value,)
entry.grid(row=0,column=1,padx=30,pady=10)

label2=tk.Label(root,text='Enter Your Password : ')
label2.grid(row=1,column=0,padx=30,pady=10)

entry2=tk.Entry(root,textvariable=pass_value,show='*')
entry2.grid(row=1,column=1,padx=30,pady=10)

button=tk.Button(root,text='Click Here...',
                 command=print_value)
# button['state']='disabled'
button.grid(row=2,column=0,padx=30,pady=10,sticky='we',
            columnspan=2)

result_label=tk.Label(root)
result_label.grid(row=3,column=0,padx=30,pady=10,sticky='we')
root.mainloop()