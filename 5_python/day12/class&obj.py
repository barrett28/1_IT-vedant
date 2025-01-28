class student:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def info(self):
        print(f'Detail of the student is name: {self.name}, age: {self.age}, gender: {self.gender}')
        
stu = student(name="bharat", age=23 ,gender="male")        

stu.info()