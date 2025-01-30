class Car:
    def __init__(self, make, model):
        self.make  = make 
        self.model = model 
        
    def get_make(self):
        return self.make
    
    def get_model(self):
        return self.model

c = Car("Ford", "Mustang")
print(c.get_make())
print(c.get_model())

print(f'Maker of this car is {c.make}')
print(f'Model of this car is {c.model}')            