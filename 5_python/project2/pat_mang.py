patients = []

def add_pat():
    pat_id = len(patients)+1
    name = input("enter patient name")
    age = input("enter patient age")
    gender = input("enter patient gender")
    address = input("enter patient address")
    # reason = input("enter patient reason")
    
    pateint = {
        "id":pat_id,
        "name":name,
        "age":age,
        "gender":gender,
        "address":address
    }
    
    patients.append(pateint)
    print("Patient added successfully")
    
    
def show_pat():
    if not patients:
        print("no records")
    else:
        for patient in patients:
            print(f"Id: {patient["id"]}, Name: {patient["name"]}, age: {patient["age"]}, gender: {patient["gender"]}, address: {patient["address"]}")
        print()
        
def del_pat():
    pat_id = int(input("enter patient id: "))
    for patient in patients:
        if patient["id"]==pat_id:
            patients.remove(patient)
            print("removed successfully")
        else:
            print("no found")
        
        
while True:
    print("\n1: Add patient")   
    print("2: Show patient")   
    print("3: Delete patient")   
    
    
    choice = int(input("enter your choice"))
    
    if choice==1:
        add_pat()
    elif choice==2:
        show_pat()
    elif choice==3:
        del_pat()
    else:
        print("wrong choice")