class Fact:
    def __init__(self, n):
        self.n = n
        
    def factorial(self):
        mulsum=1
        for i in range(self.n,0,-1):
            # print(i)
            mulsum = mulsum*i
        print(mulsum)
            
n = int(input("enter your number for factorial: "))    
    
x = Fact(n)

x.factorial()

