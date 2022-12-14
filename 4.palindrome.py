a=input("Enter a string : ")
b=tuple(a)
#print(b)
c=len(a)
d=0
'''for i in range(c):
    print(b[i])'''
for i in range(c):
    j=c-1-i
    if ord(b[i])==ord(b[j]) or ord(b[i])==(ord(b[j])+32) or ord(b[i])==ord(b[j])-32 :
        d=d+1
#        print(ord(b[i]),ord(b[j]))
#print(d)
if(d==c):
    print("Palindrome")
else:
    print("Not Palindrome")
input()