'''n=int(input("enter the number of elements"))
l=[]

for i in range(n):
    a=int(input("enter element"))
    l.append(a)
print(l)
target=int(input("enter the target"))
for i in range(len(l)):
    for j in range(i+1,len(l)):
        if((l[i]+l[j])==target):

            h=[i,j]
            print(h)'''
n=int(input("enter the number"))
s=n
l=0
while(n>0):
    r=n%10
    l=l*10+r
    n=n//10
if(l==s):
    print("it is a palindrome")
else:
    print("not a palindrome")
    
