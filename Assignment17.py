#..................Assignment 17

#..............Answer-1
from os import remove
import this


x={"Python","Java","C","C++","SQL"}
print(x)
print(type(x))

#...............Answer-2
#pending
info={"Name:Suraj","Age:20","Gender:Male"}
print(info)

#..................Answer-3
c={2,5,4,7}
print(type(c))

#.................Answer-4
d={"python","java","django"}
d1={e for e in d if e in"python"}
print(d1)

#..........................Answer-5
e={"java","python","Sql"}
e.update(["c"],["cpp"],["no sql"])
print(e)

#........................Answer-6
f={"python","django","javaScript"}
f.add(2)
print(f)

#......................Answer-7
thisset={"Python","Django","JavaScript","SQl"}
thisset.remove("SQl")
print(thisset)

#......................Answer-8
g={3,4,'abc'}
g.clear()
print(g)

#.....................Answer-9
thisset={"Python","Django","JavaScript","SQl"}
for i in thisset:
    print(i)

#answer-10
h={2,6,3,5,9}
h1=max(h)
h2=min(h)
print(h1)
print(h2)