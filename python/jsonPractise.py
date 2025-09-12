import sys
import json
def showOptions():
    option= int(input("""Choose One : -
                      1.for add student
                      2.for delete student
                      3.for exit
                      """))
    if(option==1):
        addStudent()
    elif option==2:
        deleteStudent() 
    elif option==3:
        sys.exit()
def addStudent():
    name= input('Enter the name of student : ')
    with open('st.json','r') as f:
        data = f.read()
        # print(data)
    with open('st.json','w') as f:    
        students=json.loads(data)
        # print(students)
        if len(students)>0:
            # print(type(students[len(students)-1]["id"]))
            newId=students[len(students)-1]["id"] +1
        else:
            newId =1
        students.append({"id":newId,"name":name})
        jsonData = json.dumps(students,indent=4)
        f.write(jsonData)
    showOptions()
def deleteStudent():
    delete_id=int(input('enter id : -'))
    with open('st.json','r') as f:
        data = f.read()
        students=json.loads(data)
    for index,student in enumerate(students):
        if student["id"] ==delete_id :
            i=index
            break
    students.pop(index)
    with open('st.json','w') as f:           
        jsonData = json.dumps(students,indent=4)
        f.write(jsonData)
    showOptions()


showOptions()