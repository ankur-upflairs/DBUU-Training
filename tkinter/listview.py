import tkinter as tk
import json
root=tk.Tk()

root.geometry('600x400')
root.resizable(0,0)
root.columnconfigure(0,weight=1)

# def on_select(event):
#     print(listbox.curselection())
def add_in_list():
    items.append(entry_var.get())
    list_var.set(items)
    entry_var.set('')
    
    
items=['sunil','gagan','pankaj','anuj']
list_var=tk.StringVar(value=items)
entry_var=tk.StringVar()
entry=tk.Entry(root,textvariable=entry_var)
entry.grid(row=0,column=0)
button=tk.Button(root,text='add in list',
                 command=add_in_list)
button.grid(row=1,column=0)

listbox=tk.Listbox(root,bg='lightgrey',
                   selectbackground='green',
                   selectforeground='white',
                   listvariable=list_var,
                   width=10,
                   height=6,
                   yscrollcommand=scroll.set
            )
listbox['selectmode']='single'

scroll=tk.Scrollbar(root,orient='vertical',command=listbox.yview)

listbox.grid(row=2,column=0)
scroll.grid(row=0,column=1,rowspan=3)
# listbox.bind('<<ListboxSelect>>',on_select)




# items=['sunil','gagan','pankaj','anuj']
# listbox=tk.Listbox(root,bg='lightgrey',
#                    selectbackground='green',
#                    selectforeground='white',
#             )
# listbox['selectmode']='extended'
# listbox.pack()
# listbox.bind('<<ListboxSelect>>',on_select)
# for i in items:
#     listbox.insert(tk.END,i)
# items=['abc','xyz']
# str_var=tk.StringVar(value=items)
# listview= tk.Listbox(root,listvariable=str_var)
# listview.pack()

root.mainloop()