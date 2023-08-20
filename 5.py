class Fruits:
    def __init__(self,b):
        print("constructor price: ",b)
    def Apple(self,a):
        self.a=a
        print("Apple price: ",a)
f=Fruits(1000)
f.Apple(10)
