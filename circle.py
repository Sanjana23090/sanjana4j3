class circle:
    pi=3.14159
    def __init__(self,rad):
        self.rad=rad
    def area(self):
        return circle.pi*self.rad*self.rad
    def circum(self):
        return 2*circle.pi*self.rad
obj=circle(7.5)
print("Area is ", obj.area())
print("Circumference is ",obj.circum())
    
