n=int(input("Enter a number : "))
a=[]
for i in range(n):
    a.append(int(input()))
max=a[0]
for i in range(n):
    if(a[i]>max):
        max=a[i]
print("The greatest number is : ",max)
input()