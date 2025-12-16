class SchoolManagement:
    def __init__(self):
        self.students = {}   # Stores all student records
        self.next_id = 1     # Auto-increment student ID

    # ---------------- NEW ADMISSION ----------------#
    def new_admission(self):
        print("\n---- New Admission ----")
        name = input("Enter student name: ")
        age = int(input("Enter age (5–18): "))
        student_class = int(input("Enter class (1–12): "))
        mobile = input("Enter guardian mobile number (10 digits): ")

        #---------------Age validation--------------#
        if not (5 <= age <= 18):
            print("Invalid age! Must be between 5 and 18.")
            return
        
        #------------Class validation------------#
        if not (1 <= student_class <= 12):
            print("Invalid class! Must be between 1 and 12.")
            return

        #------------Mobile validation------------#
        if not (mobile.isdigit() and len(mobile) == 10):
            print("Invalid mobile number!")
            return

        #------------Assign unique student ID------------#
        student_id = self.next_id
        self.next_id += 1

        #------------Store student info------------#
        self.students[student_id] = {
            "name": name,
            "age": age,
            "class": student_class,
            "mobile": mobile
        }

        print(f"✔ Admission successful! Student ID: {student_id}")

    # ---------------- VIEW STUDENT DETAILS ----------------#
    def view_student(self):
        print("\n---- View Student Details ----")
        sid = int(input("Enter student ID: "))

        if sid in self.students:
            print("\n Student Details:")
            info = self.students[sid]
            print(f"Name: {info['name']}")
            print(f"Age: {info['age']}")
            print(f"Class: {info['class']}")
            print(f"Guardian Mobile: {info['mobile']}")
        else:
            print("No record found for this Student ID.")

    # ---------------- UPDATE STUDENT INFO ----------------#
    def update_student(self):
        print("\n---- Update Student Info ----")
        sid = int(input("Enter student ID: "))

        if sid not in self.students:
            print("Student ID not found.")
            return

        print("""
1. Update Mobile Number
2. Update Class
""")
        choice = int(input("Choose option: "))

        if choice == 1:
            new_mobile = input("Enter new mobile number: ")
            if new_mobile.isdigit() and len(new_mobile) == 10:
                self.students[sid]["mobile"] = new_mobile
                print("Mobile number updated!")
            else:
                print("Invalid mobile number!")

        elif choice == 2:
            new_class = int(input("Enter new class (1–12): "))
            if 1 <= new_class <= 12:
                self.students[sid]["class"] = new_class
                print("Class updated!")
            else:
                print("Invalid class!")

        else:
            print("Invalid choice.")

    # ---------------- REMOVE STUDENT RECORD ----------------#
    def remove_student(self):
        print("\n---- Remove Student Record ----")
        sid = int(input("Enter student ID: "))

        if sid in self.students:
            del self.students[sid]
            print("Student record removed successfully.")
        else:
            print("No such student exists.")

    # ---------------- EXIT SYSTEM ----------------#
    def exit_system(self):
        print("Thank you for using School Management System 🙂")
        exit()



school = SchoolManagement()

while True:
    print("""
========= School Management System =========
1. New Admission
2. View Student Details
3. Update Student Info
4. Remove Student Record
5. Exit
""")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        school.new_admission()

    elif choice == 2:
        school.view_student()

    elif choice == 3:
        school.update_student()

    elif choice == 4:
        school.remove_student()

    elif choice == 5:
        school.exit_system()

    else:
        print("❌ Invalid choice, try again.")
