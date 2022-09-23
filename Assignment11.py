#,......................Assignment-11
'''
#.........................Answer-1
k= int (input("Enter the number :"))
s=0
for i in range(k+1):
    if i>=1:
        s=s+i
        print(i)
print("Sum of n natural number: ",s)


#.......................Assignmnet-2
k= int (input("Enter the number :"))
sq=0
for i in range(k+1):
    if i>=1:
        s=i*i
        sq=sq+s
        print(s)
print("Square of n natural number: ",sq)

#.......................Assignmnet-3
k= int (input("Enter the number :"))
sq=0
for i in range(k+1):
    if i>=1:
        s=i*i*i
        sq=sq+s
        print(s)
print("Cube of n natural number: ",sq)

#.......................Assignmnet-4
k= int (input("Enter the number :"))
s=0
for i in range(k+1):
    if i%2!=0:
        s=s+i
        print(i)
print("Square of n natural number: ",s)

#.......................Assignmnet-5
k= int (input("Enter the number :"))
s=0
for i in range(k+1):
    if i%2==0:
        s=s+i
        print(i)
print("Square of n natural number: ",s)

#.......................Assignmnet-6
k= int (input("Enter the number :"))
s=1
for i in range(k,0,-1):
        s=s*i
        print(i)
print("Square of n natural number: ",s)
'''

#.......................Assignmnet-7
n=int(input("Enter number:"))
count=0
while(n>0):
    count=count+1
    n=n//10
print("The number of digits in the number are:",count)


#.......................Assignmnet-8
n=int(input("Enter number:"))
total=0
while(n>0):
    d=n%10
    total=total+d
    n=n//10
print("The number of digits in the number are:",total)

