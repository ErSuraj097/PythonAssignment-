#............Assignment1-16
#.............Answer-1

a=("Java","SQL","C")
print(a)
print(type(a))

#.............Answer-2
a=("python",)
print(a)

#.............Answer-3
a=("Python")
print((a[::-1],))

#.............Answer-4
a=("Python",)
b=("Language",)
print("Before Swaping",a,b)
c=a
a=b
b=c
print("After Swaping",a, b)

#.............Answer-5
tuple1=("Python","Java","SQL")
res=tuple1.count(tuple1[0]==len(tuple1))
if res:
    print("Equal")
else:
    print("Not Equal")

#.............Answer-6 
tuple1=(100,200,300,400)
a=tuple1[0]
b=tuple1[1]
c=tuple1[2]
d=tuple1[3]

print(a)
print(b)
print(c)
print(d)

#.........Answer-7
tuple1=(1,2,3,4,5,6)
newtup=tuple1[3:5]
print(newtup)


#.............Answer-8
roll = [("a",21),("b",37),("c",11),("d",29)]   
first = 0   
last = len(roll)   
for k in range(0, last):   
    for l in range(0, last-k-1):   
        if (roll[l][first] > roll[l + 1][first]):   
            new_item = roll[l]   
            roll[l]= roll[l + 1]   
            roll[l + 1]= new_item   
print(roll)  

#..............Answer-9
tuple1=("Python",[10,20,30],(2,4,16))

li=tuple1[1]
print(li[1])

#...............Answer-10
tuple1=(11,[22,35],44,55)
li=tuple1[1]
li[0]=222
print(tuple1)
