def happynum(n):
    s,r=0,0
    while(n>0):
        r=n%10
        s=s+pow(r,2)
        n=n//10
    return s
        
x=int(input("Enter a num "))
temp=x
if(temp==1):
        print("happy num")
elif(0<temp<9):
        print("not happy")
else:
    while(temp!=1):
        temp=happynum(temp)
    
