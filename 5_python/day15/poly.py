class Animal:
    def feed(self):
        pass
    
class Lion(Animal):
    def feed(self):
        print("Feeding meat to the lion")
        

class Elephant(Animal):
    def feed(self):
        print("Feeding plants to the elephant")
        
class Bird(Animal):
    def feed(self):
        print("Feeding seeds to the bird")
        
def perform_feeding(animal):
    animal.feed()
    
lion = Lion()
elephant = Elephant()
bird = Bird()

perform_feeding(lion)
perform_feeding(elephant)
perform_feeding(bird)

