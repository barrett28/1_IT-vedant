# patients = []
# doctors = [
#     {"id": 1, "name": "Roshan Mishra", "speciality": "Orthopedic"},
#     {"id": 2, "name": "Pankaj Tripathi", "speciality": "Pediatrician"},
#     {"id": 3, "name": "Neha Saroj", "speciality": "Cardiologist"},
#     {"id": 4, "name": "Kapil Mishra", "speciality": "General Physician"}
    
# ]


# def assign_doctor(reason):
#     reason = reason.lower()
#     if "bone" in reason or "joint" in reason:
#         return doctors[0]
#     elif "child" in reason or "baby" in reason:
#         return doctors[1]
#     elif "heart" in reason:
#         return doctors[2]
#     else:
#         return doctors[3]

# # --------------------Patient Management
# def patient_info():
    
#     def add_pat():
#         pat_id = len(patients) + 1
#         name = input("Enter patient name: ")
#         age = input("Enter patient age: ")
#         gender = input("Enter patient gender: ")
#         address = input("Enter patient address: ")
#         reason = input("Enter reason for visit: ")

#         assigned_doc = assign_doctor(reason)

#         patient = {
#             "id": pat_id,
#             "name": name,
#             "age": age,
#             "gender": gender,
#             "address": address,
#             "reason": reason,
#             "doctor_id": assigned_doc["id"],
#             "doctor_name": assigned_doc["name"]
#         }

#         patients.append(patient)
#         print("Patient Added Successfully 👍🏻\n")

#     def show_patient():
#         if not patients:
#             print("No record found")
#         else:
#             print("Patient List:")
#             for patient in patients:
#                 print(f"ID: {patient['id']}, Name: {patient['name']}, Age: {patient['age']}, Gender: {patient['gender']}, "
#                       f"Address: {patient['address']}, Reason: {patient['reason']}, Assigned Doctor: {patient['doctor_name']}, "
#                       f"Doc ID: {patient['doctor_id']}")
#             print()

#     def show_doctors():
#         print("Doctor List:")
#         for doctor in doctors:
#             print(f"ID: {doctor['id']}, Name: {doctor['name']}, Speciality: {doctor['speciality']}")
#         print()

#     def pat_update():
#         patient_id = int(input("Enter patient ID: "))

#         for patient in patients:
#             if patient["id"] == patient_id:
#                 print("Enter new details (press Enter to keep current values):")

#                 new_name = input(f"New name (current: {patient['name']}): ") or patient["name"]
#                 new_age = input(f"New age (current: {patient['age']}): ") or patient["age"]
#                 new_gender = input(f"New gender (current: {patient['gender']}): ") or patient["gender"]
#                 new_address = input(f"New address (current: {patient['address']}): ") or patient["address"]
#                 new_reason = input(f"New reason (current: {patient['reason']}): ") or patient["reason"]

#                 if new_reason != patient["reason"]:
#                     assigned_doctor = assign_doctor(new_reason)
#                     patient.update({
#                         "doctor_id": assigned_doctor["id"],
#                         "doctor_name": assigned_doctor["name"]
#                     })
#                     print(f"Doctor Reassigned: {assigned_doctor['name']} (ID: {assigned_doctor['id']})")

#                 patient.update({"name": new_name, "age": new_age, "gender": new_gender, "address": new_address, "reason": new_reason})
#                 print("Patient Updated Successfully! 👍🏻")
#                 return

#         print("Patient not found!")

#     def pat_delete():
#         patient_id = int(input("Enter patient ID: "))

#         for patient in patients:
#             if patient["id"] == patient_id:
#                 patients.remove(patient)
#                 print("Patient removed successfully 👍🏻")
#                 return
#         print("Patient not found")

#     print("\nWelcome to our Patient Service 😊")

#     while True:
#         print("\n1: Add Patient")
#         print("2: Update Patient")
#         print("3: Delete Patient")
#         print("4: Show All Patients")
#         print("5: Show Doctors")
#         print("6: Exit")

#         choice = int(input("Enter your choice: "))

#         if choice == 1:
#             add_pat()
#         elif choice == 2:
#             pat_update()
#         elif choice == 3:
#             pat_delete()
#         elif choice == 4:
#             show_patient()
#         elif choice == 5:
#             show_doctors()
#         elif choice == 6:
#             print("Thank You for using the service, exiting now.")
#             break
#         else:
#             print("Invalid choice 😕, choose between 1-6.")

# # ------------------- Doctor Management
# def doc_info():
    
#     def add_doc():
#         doc_id = len(doctors) + 1
#         doc_name = input("Enter doctor name: ")
#         doc_age = input("Enter doctor age: ")
#         doc_gender = input("Enter doctor gender: ")
#         doc_speciality = input("Enter doctor speciality: ")

#         doctor = {
#             "id": doc_id,
#             "name": doc_name,
#             "age": doc_age,
#             "gender": doc_gender,
#             "speciality": doc_speciality
#         }

#         doctors.append(doctor)
#         print("Doctor Added Successfully 👍🏻")
        

#     def update_doc():
#         doc_id = int(input("Enter doctor ID: "))

#         for doctor in doctors:
#             if doctor["id"] == doc_id:
#                 print("Enter new details (press Enter to keep current values):")

#                 new_name = input(f"Update name (current: {doctor['name']}): ") or doctor["name"]
#                 new_age = input(f"Update age (current: {doctor.get('age', 'N/A')}): ") or doctor.get("age", "N/A")
#                 new_gender = input(f"Update gender (current: {doctor.get('gender', 'N/A')}): ") or doctor.get("gender", "N/A")
#                 new_speciality = input(f"Update speciality (current: {doctor['speciality']}): ") or doctor["speciality"]

#                 doctor.update({"name": new_name, "age": new_age, "gender": new_gender, "speciality": new_speciality})
#                 print("Record Updated Successfully 👍🏻")
#                 return
#         print("Record not found")

#     def doc_delete():
#         doc_id = int(input("Enter doctor ID: "))

#         for doctor in doctors:
#             if doctor["id"] == doc_id:
#                 doctors.remove(doctor)
#                 print("Record removed successfully 👍🏻")
#                 return
#         print("Doctor not found or invalid ID")

#     def show_doc():
#         if not doctors:
#             print("No doctor found")
#             return

#         print("Doctor List:")
#         for doctor in doctors:
#             print(f"ID: {doctor['id']}, Name: {doctor['name']}, Age: {doctor.get('age', 'N/A')}, Gender: {doctor.get('gender', 'N/A')}, Speciality: {doctor['speciality']}")
#         print()

#     print("\nWelcome to our Doctor Service 😊")

#     while True:
#         print("\n1: Add Doctor")
#         print("2: Update Doctor")
#         print("3: Delete Doctor")
#         print("4: Show Doctors")
#         print("5: Exit")

#         choice = int(input("Enter your choice: "))

#         if choice == 1:
#             add_doc()
#         elif choice == 2:
#             update_doc()
#         elif choice == 3:
#             doc_delete()
#         elif choice == 4:
#             show_doc()
#         elif choice == 5:
#             print("Thank You for using the service, exiting now.")
#             break
#         else:
#             print("Invalid choice 😕, choose correctly.")

# # Main Program
# while True:
#     print("\nWelcome to Hospital Management System 😊")
#     print("\n1: For Patients") 
#     print("2: For Doctors")
#     print("3: Exit")

#     choice = int(input("Enter choice: "))

#     if choice == 1:
#         patient_info()
#     elif choice == 2:
#         doc_info()
#     elif choice == 3:
#         print("Thank You for your time 😊")
#         break
#     else:
#         print("Invalid choice 🫤, please enter a valid choice.")


patients = []
doctors = [
    {"id": 1, "name": "Roshan Mishra", "speciality": "Orthopedic"},
    {"id": 2, "name": "Pankaj Tripathi", "speciality": "Pediatrician"},
    {"id": 3, "name": "Neha Saroj", "speciality": "Cardiologist"},
    {"id": 4, "name": "Kapil Mishra", "speciality": "General Physician"},
    {"id": 5, "name": "Arjun Verma", "speciality": "Orthopedic"}  # Added another orthopedic doctor
]

# Get list of doctors based on reason
def get_doctors_by_reason(reason):
    reason = reason.lower()
    if "bone" in reason or "joint" in reason:
        return [doc for doc in doctors if doc["speciality"] == "Orthopedic"]
    elif "child" in reason or "baby" in reason:
        return [doc for doc in doctors if doc["speciality"] == "Pediatrician"]
    elif "heart" in reason:
        return [doc for doc in doctors if doc["speciality"] == "Cardiologist"]
    else:
        return [doc for doc in doctors if doc["speciality"] == "General Physician"]

# Assign doctor with user selection
def assign_doctor(reason):
    available_doctors = get_doctors_by_reason(reason)

    if not available_doctors:
        print("No doctor found for this reason.")
        return None

    if len(available_doctors) == 1:
        return available_doctors[0]

    print("\nMultiple doctors available for this condition:")
    for i, doctor in enumerate(available_doctors, 1):
        print(f"{i}. {doctor['name']} (Speciality: {doctor['speciality']})")

    while True:
        try:
            choice = int(input("Enter the number of the doctor you want to assign: "))
            if 1 <= choice <= len(available_doctors):
                return available_doctors[choice - 1]
            else:
                print("Invalid choice. Please select a valid doctor number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

# Patient Management
def patient_info():
    
    def add_pat():
        pat_id = len(patients) + 1
        name = input("Enter patient name: ")
        age = input("Enter patient age: ")
        gender = input("Enter patient gender: ")
        address = input("Enter patient address: ")
        reason = input("Enter reason for visit: ")

        assigned_doc = assign_doctor(reason)

        if assigned_doc:
            patient = {
                "id": pat_id,
                "name": name,
                "age": age,
                "gender": gender,
                "address": address,
                "reason": reason,
                "doctor_id": assigned_doc["id"],
                "doctor_name": assigned_doc["name"]
            }
            patients.append(patient)
            print("Patient Added Successfully 👍🏻\n")
        else:
            print("No doctor assigned. Please check the reason and try again.")

    def show_patient():
        if not patients:
            print("No record found")
        else:
            print("Patient List:")
            for patient in patients:
                print(f"ID: {patient['id']}, Name: {patient['name']}, Age: {patient['age']}, Gender: {patient['gender']}, "
                      f"Address: {patient['address']}, Reason: {patient['reason']}, Assigned Doctor: {patient['doctor_name']}, "
                      f"Doc ID: {patient['doctor_id']}")
            print()

    def show_doctors():
        print("Doctor List:")
        for doctor in doctors:
            print(f"ID: {doctor['id']}, Name: {doctor['name']}, Speciality: {doctor['speciality']}")
        print()

    print("\nWelcome to our Patient Service 😊")

    while True:
        print("\n1: Add Patient")
        print("2: Show All Patients")
        print("3: Show Doctors")
        print("4: Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            add_pat()
        elif choice == 2:
            show_patient()
        elif choice == 3:
            show_doctors()
        elif choice == 4:
            print("Thank You for using the service, exiting now.")
            break
        else:
            print("Invalid choice 😕, choose between 1-4.")

