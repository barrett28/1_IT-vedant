class Parent:
    def parent_property(self):
        print("this is parent property")
        
class Child(Parent):
    def child_property(self):
        print("this is child property")
        
c = Child()
p = Parent()
p.parent_property()
c.child_property()
c.parent_property()