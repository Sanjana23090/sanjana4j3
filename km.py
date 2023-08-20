def fact(x):
    if(x==1):
        return 1
    return x*fact(x-1)
num=int(input("Enter "))
temp=num
s=0
while(num>0):
    r=num%10
    s+=fact(r)
    num=num//10
if(s==temp):
    print("KM")
else:
    print("No")
