sum,dig=0,0
n=int(input())
temp=n
while(n>0):
    dig+=1
    n=n//10
n=temp
while(n!=0):
    r=n%10
    sum+=r**dig
    n=n//10
if(sum==temp):
    print("Armstrong number")
else:
    print("Not an armstrong number")
