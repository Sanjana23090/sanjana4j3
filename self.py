#prog to create self arg and access obj
class abc:                #2
    attribute1=10       #3
    def display(self):   #6     #self arg is used to access a class var from func
        print("this is in class ")  #7
obj=abc()                 #1
print(obj.attribute1)   #4
obj.display()             #5
