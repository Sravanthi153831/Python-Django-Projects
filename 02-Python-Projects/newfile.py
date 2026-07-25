employees = {}

while True:
    print("\n===== Employee Management System =====")
    print("1. Add Employee")
    print("2. View Employees")
    print("3. Search Employee")
    print("4. Update Employee")
    print("5. Delete Employee")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        emp_id = input("Enter Employee ID: ")
        name = input("Enter Name: ")
        salary = input("Enter Salary: ")

        employees[emp_id] = {
            "Name": name,
            "Salary": salary
        }

        print("✅ Employee Added Successfully!")

    elif choice == "2":
        if employees:
            for emp_id, details in employees.items():
                print("\nEmployee ID:", emp_id)
                print("Name:", details["Name"])
                print("Salary:", details["Salary"])
        else:
            print("No Employees Found!")

    elif choice == "3":
        emp_id = input("Enter Employee ID to Search: ")

        if emp_id in employees:
            print("✅ Employee Found!")
            print("Employee ID:", emp_id)
            print("Name:", employees[emp_id]["Name"])
            print("Salary:", employees[emp_id]["Salary"])
        else:
            print("❌ Employee Not Found!")

    elif choice == "6":
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")