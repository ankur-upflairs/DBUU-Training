x=34
# print(x,end='&')
y='hello'
z=x
a=None
# print(x,y,a,sep='-')
del x
# print(x)
""" 1. can contain digit , no. , _
2. can't start with number
3. we can't use reserve keywords as name
"""
#int => no without decimal
b=56
# print(type(b))
#float => no with decimal
c=45.7
# print(c,type(c))
#complex => real + imagenary part
d= 5+6j
# print(d,type(d))
# print(d.imag,d.real)
#booleans =>
e=True
# print(e,type(e))
#String => collection of characters
f= "hello"
g='everyone'
# print(f,g)
i= """hi ,
my name is pawan"""
# print(i)
j=f"{f}, everyone"
# print(j)
k="hello , {} ,{}"
# print(k.format("gagan","how are you?"))
email="""
Hello Sir/Ma'am, {name}
        {content}
        date:- {time}
"""
# print(email.format(name="sunil kumar",
                #    content="how are you?",
                #    time="12-09-2025"))
#list => 
l=[23,"xyz",5.6,True]
# print(type(l))
# indexing=>
# print(l[2])
# print(l[-3])
l[0]=45
# print(l)
m='hello'
# n=list(m)
# print(n)
#tuple => immutable , ordered , collection
#data type 
o=(34,23,67,True)
# print(type(o))
# print(o[1])
p=(45,)
# print(type(p))
#ages=(34,23,67)  => change 23 to 89 by using list
ages=(34,23,67)
ages_list=list(ages)
# print(ages_list)
ages_list[1]=89
ages=tuple(ages_list)
# print(ages)
#range =>
# print(range(5))
# for i in range(5):
#     print(i)
# for i in range(2,9):
#     print(i)
# for i in range(1,7,2):
    # print(i)
#sets=> does not allow duplicate
#unordered ,
#mutable 
q= {34,56,78,56}
# print(q)
#dict=> 
r={1:'a',2:'b','c':'d'}
# print(r[1])
# print(r.get(2))
# for key in r:
#     print(key)
# print(r.values())
# for i,j in r.items():
#     print(i,j)
# print(r.keys())
# print(r.clear())
# print(r)
# print(r.pop(2))
# r.popitem()
# r['d']=45
# print(r)

