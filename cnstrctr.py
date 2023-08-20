class abc:                #2
    def __init__(self,value):   #3     #
        print("this is in class ")      #4
        self.value=value       #5          #self reflects 100 and gives permission to store 100 in value
        print("The value is ",value)  #6
obj=abc(100)                 #1
