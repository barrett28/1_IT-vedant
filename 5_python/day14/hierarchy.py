class Parent:
    def __init__(self, name):
        self.name = name
        print("this is the parent class cons")
        
    def parent_prop(self):
        print(f"name of the parent is {self.name}")
        
class Son(Parent):
    def __init__(self, name, sonName):
        super().__init__(name)
        self.sonName = sonName
        
    def son_prop(self):
        print(f"name of the son is {self.sonName}")
        
class Daughter(Parent):
    # super.__init__()
    def __init__(self, name, DauNmae):
        super().__init__(name)
        self.DauName = DauNmae
        
    def dau_prop(self):
        print(f"Daughter name is {self.DauName}")
        
s = Son(name="papa", sonName="beta")
s.parent_prop()
s.son_prop()