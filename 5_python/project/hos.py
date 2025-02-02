
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

def pat_update():
    patient_id = int(input("enter patient id: "))
    
    for patient in patients:
        if patient["id"]==patient_id:
            print("enter new details \nenter to skip the current updating field")
            new_name = input(f"New name (current name: {patient["name"]}): ") or patient["name"]
            new_age = input(f"New age (current age is {patient["age"]}): ") or patient["age"]
            new_gender = input(f"New gender (current gender is {patient["gender"]}): ") or patient["gender"]
            new_address = input(f"New Address (current address is {patient["address"]}): ") or patient["address"]
            
            patient.update({"name": new_name, "age":new_age, "gender":new_gender, "address":new_address})
            print("Patient Updated Successfully")


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
    print("\n1: Add Patient")
    print("2: Update Patient")
    print("3: Delete Patient")
    print("4: Show All Patient")
    print("5: Exit")
    
    choice = int(input("Enter your choice: "))
    
    if choice==1:
        add_pat()
    elif choice==2:
        pat_update()
    elif choice==3:
        pat_delete()
    elif choice==4:
        show_patient()
    elif choice==5:
        print("exiting from the service")
        break
    else:
        print("invalid choice, choose in between 1-5")
        
        
        
# doctors = []

# def add_doc():
#     doc_id = len(doctors)+1
#     doc_name = input("Enter doc name: ")
#     doc_age = input("Enter doc age: ")
#     doc_gender = input("Enter doc gender: ")
#     doc_speciality = input("Enter doc speciality: ")
    
#     doctor = {
#         "doc_name" = doc_name
#     }