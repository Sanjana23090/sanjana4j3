class abc:
    even=[]
    odd=[]
    def __init__(self,num):
        self.num=num
        if num%2==0:
            abc.even.append(num) #appending even attribute of class abc
        else:
            abc.odd.append(num)
n1=abc(11)
n2=abc(12)
n3=abc(13)
n4=abc(28)
n5=abc(7)
print("even number list is ",abc.even)
print("odd number list is ",abc.odd)

        
