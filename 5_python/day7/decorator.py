def shop(gift):
    def wrap():
        print("red color")
        gift()
    return wrap

@shop
def gift():
    print('watch')
    
gift()


