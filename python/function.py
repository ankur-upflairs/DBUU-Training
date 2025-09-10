# function => it a reusable block of code 
#to perform some specific task
#declaration
# def sum(a,b):
#     print('sum is',a+b)
# calling 
# sum(5,8)
# def sum(a,b):
#     return a+b
# print(sum(5,6))
#make a function to calculate sqrt of any no.
#make a function to calculate interest
# def sqrt(a):
#     return a**0.5
# x=sqrt(25)
# print(x)
# def calculate_interest(p,t,r):
#     return (p*t*r)/100
# i = calculate_interest(1000,2,10)
# print(i)
# def greet():
#     print('hello')
# g=greet
# g()
# def x():
#     def y():
#         print('hello everyone')
#     return y
# a=x()
# a()
# def bank_interest(r,fnc):
#     x=r*2
#     y=fnc(x)
#     return y 

# def bob(a):
#     return a/3
# bob_interest = bank_interest(10,bob)
# print(bob_interest)
#global , local , non-local 
x=15#global 
# def multiply():
#     x=20
#     x+=3#x=x+3 
#     print(x)
# multiply()
# print(x)
# def multiply():
#     global x
#     x+=3#x=x+3
#     print(x)
# multiply()
# print(x)
# def sum(a,b):
#     x=a+b 
#     print(x)
#     def multiply():
#         nonlocal x
#         x=10
#         print(x)
#     multiply()
#     print(x)
# sum(12,9)
# def addAndPerform(n,fnc):
#     n=n+4
#     y=fnc(n)
#     return y 
# def multiplyBy5(n):
#     return n*5
# x= addAndPerform(10,multiplyBy5)
# print(x)
# def sum(a,b=6):
#     return a+b
# print(sum(5))
# def greet(name,surname):
    # print(f"hello, {name} {surname}")
# greet('sunil','kumar')    
# greet(surname='kumar',name='sunil')     

# def sum(*args):
#     print(args)
#     s=0
#     for i in args:
#         s+=i
#     print(s)
# sum(3,5,6)

#multiply and average 
#all operations using single function
# sum(op,*args) op='+'
# def operations(op,*args):
#     if(op=='+'):
#         sum(*args)
#     elif op=='*':
#         m=1
#         for i in args:
#             m*=i
#         print(m)
# operations('+',3,4,5)   
# def printNo(n):
#     if n==0:
#         return
#     printNo(n-1)
#     print(n)
# printNo(10)
# def fact(n):
#     if n==1:
#         return 1 
#     return n * fact(n-1)
# return n * fact(n-1)
#n* n-1 * fact(n-2)
#n * n-1 * n-2 * fact(n-3)
# print(fact(5))
#find the average of nos using recursion

# def average(*n ,y=1):
#     x=len(n)
#     if(len(n)==0):
#         return 0
#     n=list(n)
#     l=n[-1]
#     n.pop()
#     # print(n)
#     sum= l + average(*n,y=2)
#     # print(sum,x)
#     if y==1:
#         return sum / x 
#     else :
#         return sum       
# print(average(3,4,5))
# def average(*n ,total=0):
#     if total==0:
#         total=len(n)
#     if(len(n)==0):
#         return 0
#     n=list(n)
#     l=n[-1]
#     n.pop()
#     # print(n)
#     return l /total + average(*n,total=total)   
# print(average(3,4,5))
marks={
    'sub1':12,
    'sub2':14,
    'sub3':15
}
def totalMarks(**kwargs):
    print(kwargs)
    s=0
    for i,j in kwargs.items():
        s+=j
    print(s)
# totalMarks(sub1=marks['sub1'],sub2=marks['sub2'],sub3=marks['sub3'])
# totalMarks(**marks)
# anonymus function => function without name
lambda x,y:x+y
# print((lambda x,y:x+y)(4,5))
add=lambda x,y:x+y 
# print(add(45,3))
def double(x):
    return x*2
d=list(map(double,[3,4,5,6]))
print(d)
# make a list of given list using mapand lambda

