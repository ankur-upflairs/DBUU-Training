# a=[3,4,5,7,9]
# for i in a:
#     print(i)
# for i in range(len(a)):
#     print(i)
#delete a element from list at specified 
#position
# a=[3,5,7,9,12]
# index=2
# b=[]
# for i in a:
#     if(a.index(i)== index):
#         continue
#     else:
#         b.append(i)
# print(b)
# a=[3,5,7,9,12,5]
# print(a.append(34))
# a.clear()
# a.extend([45,23])
# print(a.count(5))
# print(a)
# make a progamme to perform crud operations
# on list 
#1.ask user what he wants -delete,update,insert,just read
#2.and index and value (if neccessary)
#3.perform operations according to preference
# a=[3,4,5,6,7]
# op=int(input("""Enter your preference -
#              1. delete
#              2.insert
#              3.update
#              4.read 
#              """))
# i=None
# if op==1:
#     i=int(input('enter index no. - '))
#     a.pop(i)
# elif op==2:
#     i=int(input('enter index no. - '))
#     v=input('enter value : - ')
#     a.insert(i,v)
# elif op==3:    
#     i=int(input('enter index no. - '))
#     v=input('enter value : - ')
#     a[i]=v
# elif op==4:
#     print('list is -',a)
# else :
#     print('preference not match')
# print(a)
a=[3,5,7,9,12,5]
# print(a.index(5,2))
# print(a.remove(9))
# a.reverse()
# a.sort(reverse=True)
# b=a.copy()
# print(a,b)
# b=a.copy()
# b[0]=8
# print(a,b)
#tupple => immutable
# b=(4,5,6)
# print(b.index(5))
