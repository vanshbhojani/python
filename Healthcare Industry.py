class ClinicAppointment:
    def __init__(self):
        #--------------Allowed time slots--------------#
        self.time_slots = ["10am", "11am", "12pm", "2pm", "3pm"]

        self.appointments = {}

    # ---------------- BOOK APPOINTMENT ----------------#
    def book_appointment(self):
        name = input("Enter patient name: ")
        age = int(input("Enter age: "))
        mobile = input("Enter mobile number: ")
        doctor = input("Enter preferred doctor name: ")

        #----------------Initialize doctor in system-------------#
        if doctor not in self.appointments:
            self.appointments[doctor] = {slot: [] for slot in self.time_slots}

        print("\nAvailable Time Slots:")
        for i, slot in enumerate(self.time_slots, 1):
            print(f"{i}. {slot}")

        slot_choice = int(input("Choose a time slot (1-5): "))
        if not (1 <= slot_choice <= len(self.time_slots)):
            print("Invalid slot selection!")
            return

        chosen_slot = self.time_slots[slot_choice - 1]

        #-----------Check availability (max 3 per slot)------------#
        if len(self.appointments[doctor][chosen_slot]) >= 3:
            print("Slot full! Please choose another time.")
            return

        #-------Save appointment--------#
        patient_data = {
            "name": name,
            "age": age,
            "mobile": mobile,
            "doctor": doctor,
            "slot": chosen_slot
        }

        self.appointments[doctor][chosen_slot].append(patient_data)
        print(f"Appointment booked for {name} at {chosen_slot} with Dr.{doctor}")

#------------VIEW APPOINTMENT-------------# 
    def view_appointment(self, mobile):
        print("\n Searching appointments...")
        for doctor in self.appointments:
            for slot in self.time_slots:
                for p in self.appointments[doctor][slot]:
                    if p["mobile"] == mobile:
                        print("\n Appointment Details:")
                        print(f"Name: {p['name']}")
                        print(f"Age: {p['age']}")
                        print(f"Doctor: {p['doctor']}")
                        print(f"Time Slot: {p['slot']}")
                        return
        print("No appointment found for this mobile number.")

#---------------CANCEL APPOINTMENT---------------# 
    def cancel_appointment(self, mobile):
        for doctor in self.appointments:
            for slot in self.time_slots:
                for p in self.appointments[doctor][slot]:
                    if p["mobile"] == mobile:
                        self.appointments[doctor][slot].remove(p)
                        print(f"✔ Appointment for {p['name']} canceled successfully.")
                        return
        print("No appointment found to cancel.")

#--------------SHOW DOCTOR AVAILABILITY----------------# 
    def doctor_availability(self, doctor):
        if doctor not in self.appointments:
            print(f"Doctor {doctor} has no appointments yet.")
            return

        print(f"\n Availability for Dr.{doctor}:")
        for slot in self.time_slots:
            count = len(self.appointments[doctor][slot])
            print(f"{slot}: {3 - count} slots available")


clinic = ClinicAppointment()

while True:
    print("""
---------- Clinic Appointment System ----------
1. Book Appointment
2. View Appointment
3. Cancel Appointment
4. Doctor Availability
5. Exit
""")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        clinic.book_appointment()

    elif choice == 2:
        mobile = input("Enter mobile number: ")
        clinic.view_appointment(mobile)

    elif choice == 3:
        mobile = input("Enter mobile number to cancel: ")
        clinic.cancel_appointment(mobile)

    elif choice == 4:
        doctor = input("Enter doctor name: ")
        clinic.doctor_availability(doctor)

    elif choice == 5:
        print("Exiting system...")
        break

    else:
        print("Invalid choice, try again!")
