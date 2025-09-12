import json
with open('students.json','r')as f:
    data = f.read()
    students= json.loads(data)
    # print(students)
students[0]["name"]='pawan'
# print(students)

with open('students.json','w') as f:
    jsonData=json.dumps(students)
    # print(jsonData)
    f.write(jsonData)
 
    
