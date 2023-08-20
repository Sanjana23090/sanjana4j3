class abc:
    class_var=0
    def __init__(self,var):   
        abc.class_var +=1
        self.var=var
        print("the obj value is ",var)      
        print("The class value is ",abc.class_var)  
obj1=abc(100)
obj2=abc(101)
obj3=abc(102)
