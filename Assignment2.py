
#...........Assignment 2.............

#.......Answer1
from ast import keyword
from pkgutil import ImpImporter
from re import M


print("Learning Python") #print function

#.......Answer2 
'''
This is 
multuLine
Comment'''
name= "Suraj Yadav "
age=20
yrExp=1.2
quali=10+2
stmnt = True
print(name,age,yrExp,quali,stmnt)


#.......Answer3
'''Type of variable - Two Types 
1. Local Variable 
2. Global Variable '''

rollNo=20
name= "Suraj Yadav "
yrExp=1.2
cmp=10+2j
stmnt = True
print ("Data Type of all variable ")
print(type(rollNo))
print(type(name))
print(type(yrExp))
print(type(cmp))
print(type(stmnt))

#..........Answer 4
a="Django"
b="2800"
print(a,"of id=",id(a))
print(b,"of id=",id(b))

#..........Answer 5
rollNo=20
name= "Suraj Yadav "
yrExp=1.2
cmp=10+2j
stmnt = True
print(rollNo,"of data type", type(rollNo), "for id",id(rollNo))
print(name,"of data type", type(name), "for id",id(name))
print(yrExp,"of data type", type(yrExp), "for id",id(yrExp))
print(cmp,"of data type", type(cmp), "for id",id(cmp))
print(stmnt,"of data type", type(stmnt), "for id",id(stmnt))

#.........Answer 6
import keyword
print(keyword.kwlist)

#.........Answer 7
info =help(keyword.kwlist)
print(info)

#...........Answer 8
import assignment1
print(assignment1.name)

#..........Assignment 10
from datetime import*
dt= datetime.today();
print(dt)

dtm= dt.strftime("%m-%d-%Y and %H:%M")
print("Current Date = ",dtm)
