print("enter the 1 st matrix :")
a=[]
for i in range(3):
    a1=[]
    for j in range(3):
        input1=int(input())
        a1.append(input1)
    a.append(a1)
print(a)

print("enter the 2nd matrix :")
b=[]
for i in range(3):
    b1=[]
    for j in range(3):
        input1=int(input())
        b1.append(input1)
    b.append(b1)
print(b)

# logic
r=[]
for i in range(len(a)):
    r1=[]
    for j in range(len(a[0])):
       s = a[i][j]-b[i][j]
       r1.append(s)
    r.append(r1)
print("difference of matrices :",r) 
       
     


