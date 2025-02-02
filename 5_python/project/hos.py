
patients = []

def add_pat():
    pat_id = len(patients)+1
    name = input("Enter patient name: ")
    age = input("Enter patient age: ")
    gender = input("Enter patient gender: ")
    address = input("Enter patient address: ")
    
    patient = {
        "id":pat_id,
        "name": name,
        "age":age,
        "gender": gender,
        "address": address
    }
    
    patients.append(patient)
    print("Patient Added Successfully\n")
    
def show_patient():
    if not patients:
        print("No record found")
    else:
        print("patient list:")
        for patient in patients:
            print(f"ID: {patient["id"]}, name: {patient["name"]}, Age: {patient["age"]}, Gender: {patient["gender"]}, Address: {patient["address"]}")
        print()
        
def pat_delete():
    patient_id = int(input("enter patient ID: "))
    
    for patient in patients:
        if patient["id"]==patient_id:
            patients.remove(patient)
            print("patient removed successfully")
            return
    print("patient not found")
    
    
print("Welcome to our service 😊")
# print("\n1.Add, 2.update, 3.delete, 4.show")

while True:
    print("\n 1: Add Patient")
    # print("\n 2: Update Patient")
    print("\n 3: Delete Patient")
    print("\n 4: Show All Patient")
    print("\n 5: Exit")
    
    choice = int(input("Enter your choice: "))
    
    if choice==1:
        add_pat()
    elif choice==3:
        pat_delete()
    elif choice==4:
        show_patient()
    elif choice==5:
        print("exiting from the service")
    else:
        print("invalid choice, choose in between 1-5")