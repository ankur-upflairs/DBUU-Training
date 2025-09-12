# class Person:
#     species='Homosepiens'#class variable
#     def __init__(self,name,age):
#         self.name=name #intance variable 
#         self.age=age 
#     def show_details(self):
#         return f"Name:-{self.name} and Age:-{self.age}"
#     def __str__(self):
#         return f"Class: Person - Object:-name={self.name}"
    
# class Teacher(Person):
#     def __init__(self, name, age,subject):
#         super().__init__(name,age)
#         self.subject=subject
#     def show_details(self):
#         return f"Occupation:Teacher , {super().show_details()}"

# teacher1=Teacher('Gagan',23,'Math')
# print(teacher1.name,teacher1.show_details()) 
# person1=Person('pawan',34)

# print(person1.name,person1.age ,Person.species)
# person1.show_details()
# Person.show_details(person1)

# print(person1)

# def multiply(a,b=1,c=1,d=1):
#     return a*b*c*d
# def multiply(*args):
#     m=1
#     for i in args:
#         m*=i
#     return m

# print(multiply(4,5))
# class Animal:
#     def __init__(self,name,color,breed):
#         self.name=name #public variable
#         self._color=color #protected
#         self.__breed=breed #private 
#     def get_breed(self):
#         return self.__breed

# class Dog(Animal):
#     def __init__(self, name, color, breed): 
#         super().__init__(name, color, breed)
# pitbull=Dog('jeffy','brown','pit')
# print(pitbull.name ,pitbull._color)
# print(pitbull.get_breed())

class D:
    def __init__(self):
        print('d')
class A(D):
    def __init__(self):
        print('a')

class B:
    def __init__(self):
        print('b')
class C(A,B):
    def __init__(self):
        print('c')
        # super().__init__()
        A.__init__()
        B.__init__()
c=C()

        





