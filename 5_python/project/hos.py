
patients = []
doctors = []

def patient_info():
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
        print("Patient Added Successfully 👍🏻\n")
        
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
                print("Patient Updated Successfully 👍🏻")


    def pat_delete():
        patient_id = int(input("enter patient ID: "))
        
        for patient in patients:
            if patient["id"]==patient_id:
                patients.remove(patient)
                print("patient removed successfully 👍🏻")
                return
        print("patient not found")
              
    print("\nWelcome to our Patients service 😊")
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
            print("Thank You for using it, exiting from the service")
            break
        else:
            print("invalid choice 😕, choose in between 1-5")
        
        

def doc_info():
    def add_doc():
        doc_id = len(doctors)+1
        doc_name = input("Enter doc name: ")
        doc_age = input("Enter doc age: ")
        doc_gender = input("Enter doc gender: ")
        doc_speciality = input("Enter doc speciality: ")
        
        doctor = {
            "doc_id":doc_id,
            "doc_name": doc_name,
            "doc_age": doc_age,
            "doc_gender": doc_gender,
            "doc_speciality": doc_speciality            
        }
        
        doctors.append(doctor)
        print("Doctor Added Successfully 👍🏻")
        
    def update_doc():
        doc_id = int(input("Enter Id: "))
        
        for doctor in doctors:
            if doctor["doc_id"]==doc_id:
                new_doc_name = input(f"Update name: (current name is {doctor["doc_name"]}): ") or doctor["doc_name"]
                new_doc_age = input(f"Update age: (current age {doctor["doc_age"]}): ") or doctor["doc_age"]
                new_doc_gender = input(f"Update Gender: (current gender is {doctor["doc_gender"]}): ") or doctor["doc_gender"]
                new_doc_spec = input(f"Update speciality: (current speciality is {doctor["doc_speciality"]}): ") or doctor["doc_speciality"]
                
                doctor.update({"doc_name":new_doc_name, "doc_age":new_doc_age, "doc_gender":new_doc_gender, "doc_speciality":new_doc_spec})
                print("Record Updated Successfully 👍🏻")
                return
        print("record not found")
        
        
    def doc_delete():
        doc_id = int(input("enter doctor id: "))
        
        for doctor in doctors:
            if doctor["doc_id"]==doc_id:
                doctors.remove(doctor)
                print("record removed successfully 👍🏻")
                return
        print("doctor not found or invalid ID")
        
    def show_doc():
        if not doctors:
            print("No patient found")
            return

        for doctor in doctors:
            print(f"Id: {doctor["doc_id"]}, Doc Name: {doctor["doc_name"]}, Doc Age: {doctor["doc_age"]}, Doc Gender: {doctor["doc_gender"]}, Speciality: {doctor["doc_speciality"]}")
            
    
    print("Welcome to our Doctors service 😊")
    
    while True:
        print("\n1: Add Doctor")
        print("2: Update Doctor")
        print("3: Delete Doctor")
        print("4: Show Doctor")
        print("5: Exit")
        
        choice = int(input("Enter your choice: "))
        
        if choice==1:
            add_doc()
        elif choice==2:
            update_doc()
        elif choice==3:
            doc_delete()
        elif choice==4:
            show_doc()
        elif choice==5:
            print("Thank You for using it, Exiting from the service")
            break
        else:
            print("Invalid choice 😕, choose choice correctly")
                     

while True:
    print("\nWelcome to Hospital Management System 😊")
    print("\n1: For Patients") 
    print("2: For Doctors")
    print("3: Exit")
    
    choice = int(input("Enter choice: "))
    
    if choice==1:
        patient_info()
    elif choice==2:
        doc_info()
    elif choice==3:
        print("Thank You for your time 😊")
        break
    else:
        print("Invalid choice, please enter valid choice")