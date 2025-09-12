import tkinter as tk
import json
root=tk.Tk()

root.geometry('600x400')
root.resizable(0,0)

def load_json():
    # students=None
    with open('st.json','r') as f:
        data = f.read()
        # print(data)
        students=json.loads(data)
    return students
def update_json(jsonData):
    with open('st.json','w') as f:
        f.write(jsonData)
def add_student(name):
    students=load_json()
    if len(students)>0:
        newId=students[len(students)-1]["id"] +1
    else:
        newId =1
    students.append({"id":newId,"name":name})
    jsonData = json.dumps(students,indent=4) 
    update_json(jsonData) 
def deleteStudent():
    students=load_json()
    index=listbox.curselection()[0]
    if not index:
        return
    students.pop(index)
    jsonData = json.dumps(students,indent=4)
    update_json(jsonData)
    display_students()
listbox=None
def display_students():
    students=load_json()
    global listbox
    listbox= tk.Listbox(studentFrame,)
    listbox.grid(row=1,column=0,sticky='nswe')       
    for student in students:
        listbox.insert('end',f"{student["id"]}. {student["name"]}")
        
def add_in_list():
    add_student(entry_var.get())
    entry_var.set('')
    display_students()
    

entry_var=tk.StringVar()
    
studentFrame=tk.Frame(root)
studentFrame.grid(row=0,column=0)
inputFrame= tk.Frame(studentFrame)
inputFrame.grid(row=0,column=0)
entry=tk.Entry(inputFrame,textvariable=entry_var)
entry.grid(row=0,column=0)
button=tk.Button(inputFrame,text='add in list',
                 command=add_in_list)
button.grid(row=0,column=1)
button1=tk.Button(studentFrame,text='delete',
                  command=deleteStudent)
button1.grid(row=2,column=0)
display_students()

root.mainloop()
