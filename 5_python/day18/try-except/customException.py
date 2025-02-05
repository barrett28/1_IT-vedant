class error(Exception):
    pass

def speed_limit():
    speed = 5
    
    try:
        if speed<50:
            raise error("you are not a rider")
        print("you are a rider")
    except error as e:
        print(e)
        
speed_limit()