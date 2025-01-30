class GrandParent:
    def __init__(self, name, rollno):
        self.name = name 
        self.rollno = rollno
        print("grandparent ka constructor")
        
    def grand_property(self):
        print(f"name of the student is {self.name} and rollNO is {self.rollno}")
        
class Parent(GrandParent):
    def __init__(self, name, rollno, address):
        self.address = address
        super().__init__(name, rollno)
        print("parent ka constructor")
    
    def parent_property(self):
        print(f"adress of the student is {self.address}")   
        
class Child(Parent):
    def __init__(self, name, rollno, address, div):
        self.div = div
        super().__init__(name, rollno, address) 
        print("child ka constructor ")
        
    def child_property(self):
        print(f"division of the student is {self.div}")
    
c = Child(name="Bharat", rollno=55, address="Kalyan", div="A")
c.grand_property()