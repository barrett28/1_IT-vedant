from database import connect_db

def add_pat():
    conn = connect_db()
    cursor = conn.cursor()
    
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    gender = input("Enter your gender: ")
    address = input("Enter your address: ")
    
    sql = "INSERT INTO patients (name, age, gender, address) VALUES (%s %s %s %s)"
    
    cursor.execute(sql, (name, age, gender, address))
    
    conn.commit()
    print("added successfully")
    
    cursor.close()
    conn.close()