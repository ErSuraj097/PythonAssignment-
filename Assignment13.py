'''#................Assignment-13
#..........Answer-1
li=["Java","Python,","SQL","C"]
print(li)

#..........Answer-2
li=["Python",2800,3.5,"Django"]
c=0
for i in li:
    c+=1
for j in range(c):
    print(type(li[j]))

#..........Answer-3
print("List : ",["Python",2800,3.5,"Django"])
print("Last item of list :", li[-1:])

#..............Answer-4

li=["Java","SQL","C","Reactnative","Javascript","Python"]
li[1]="NoSQL"
li[3]="Fluter"
print(li)

#.........Amswer-5
li=["Java","SQL","C","Reactnative",]
li.append("Python")
print(li)

#...........Answer-6
firstList=["Java","Python","SQL"]
secondList=["C","Cpp","NoSQL"]
for i in secondList:
    firstList.append(i)
print(firstList)

#............Answer7
li=["Java","SQL","C","Reactnative","Javascript","Python"]
c=0
for i in li:
    c+=1
    print(c,". ",i)
#for i in li:
print(li[0:6])
'''
#..............Answer-8
li=["Java","SQL","C","Reactnative","Javascript","Python"]
li.sort()
print(li)

#...........Answer-9
n=int(input("Enter the number of cities : "))
a=[]
for i in range(n):
    city=input("Enter the city name ")
    a.append(city)
print(a)

