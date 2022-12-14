a=int(input("Enter an integer: "))
c=0
i=1
for i in range(1,(a+1)):
    if(a%i==0):
        c=c+1
if(c==2):
    print("Prime")
else:
    print("Not Prime")