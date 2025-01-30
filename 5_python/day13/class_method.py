class Bike:
    hiked_price = 0
    
    @classmethod
    def increased_price(cls, price):
        cls.hiked_price = price*1.2
        
yamaha = Bike()
apache = Bike()
ninja = Bike()

yamaha.increased_price(10000)
apache.increased_price(500)
ninja.increased_price(10)

print(f'Hiked Priced after increament in yamaha is {yamaha.hiked_price}')
print(f'Hiked Priced after increament in apache is {apache.hiked_price}')
print(f'Hiked Priced after increament in ninja is {ninja.hiked_price}')