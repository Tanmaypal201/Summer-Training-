'''Create a Rectangle class with Length and Breadth.
Methods: area(), perimeter(), check_square().
'''

class Reactangle():
    length=0
    breath=0
    
    def __init__(self,l,b):
        self.length=l
        self.breath=b
    
    def area(self):
        print(f"Area of the Rectangle:{self.length*self.breath}")
    
    def perimeter(self):
        print(f"Premeter of the Rectangle:{2*(self.length + self.breath)}")
    def check_square(self):
        if(self.length==self.breath):
            print("It is a Square")
            return
        print("Is it a Rectangle")
r1=Reactangle(3,3)
r1.area();
r1.perimeter()
r1.check_square()
