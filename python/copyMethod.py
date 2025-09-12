import copy
person={
    "name":'sunil',
    "age":34,
    "contact":{
        "email":'a@b.com'
    }
}
# person1=person.copy()
# person["age"]=50
# # print(person,person1)
# person["contact"]["email"]="x@y.com"
# print(person,person1)
# person2=copy.deepcopy(person)
# print(person2)
person["contact"]["email"]='x@y.com'
# print(person,person2)
