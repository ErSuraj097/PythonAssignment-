#.........................Assignment -14 
#..................Answer- 1

li=[]
n= int(input("Enter the number :"))
for i in range(n+1):
    if i>=1:
        li.append(i)
print(li)

# ,.............. Answer-2
li=[]
n= int(input("Enter the number :"))

for i in range(n+1):
    if i%2!=0:
        li.append(i)
print(li)

# ,.............. Answer-3
li=[]
n= int(input("Enter the number :"))

for i in range(n+1):
    if i%2==0:
        li.append(i)
print(li)

# ,.............. Answer-4
li=[]
n=int(input("Enter the no of element :")) 
for i in range(n):
    k=int(input("Enter the number in List :"))
    li.append(k)
print("List : ",li)
print("Greater Value in List: ",max(li))


# ,.............. Answer-5
li=[]
n=int(input("Enter the no of element :")) 
for i in range(n):
    k=int(input("Enter the number in List :"))
    li.append(k)
print("List : ",li)
print("Greater Value in List: ",min(li))

#........Answer-6
li=[]
n=int(input("Enter the no of element :")) 
for i in range(n):
    k=int(input("Enter the number in List :"))
    li.append(k)
print("List : ",li)
s=0
for i in li:
    s=s+i
print("Sum of element :", s)

#.................Answer-7

#answer-9
l=[2,5,9,8,4,1,2,7]
print(l.count(7))


#answer-10
l1=[2,50,16,9,7]
l1.sort()
print("Sorted List : ",l1)


