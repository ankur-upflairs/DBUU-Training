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
studentFrame=tk.Frame(root)
studentFrame.pack()
students=load_json()

for student in students:
    label=tk.Label(studentFrame)
    label["text"]=f"{student["id"]}.Name : - {student["name"]}"
    label.pack(pady=10)

root.mainloop()
