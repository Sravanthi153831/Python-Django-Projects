import sqlite3

conn = sqlite3.connect("employees.db")
cursor = conn.cursor()

# Create Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS employees(
    emp_id INTEGER PRIMARY KEY,
    name TEXT,
    department TEXT,
    salary REAL
)
""")

conn.commit()

while True:
    print("\n===== Employee Management System =====")
    print("1. View Employees")
    print("2. Add Employee")
    print("3. Search Employee")
    print("4. Update Employee")
    print("5. Delete Employee")
    print("6. Exit")

    choice = input("Enter your choice: ")

    # View Employees
    if choice == "1":
        cursor.execute("SELECT * FROM employees")
        employees = cursor.fetchall()

        print("\nEmployee List")
        print("----------------------------------------")

        for employee in employees:
            print(employee)

    # Add Employee
    elif choice == "2":
        emp_id = int(input("Enter Employee ID: "))
        name = input("Enter Employee Name: ")
        department = input("Enter Department: ")
        salary = float(input("Enter Salary: "))

        cursor.execute(
            "INSERT INTO employees VALUES (?, ?, ?, ?)",
            (emp_id, name, department, salary)
        )

        conn.commit()
        print("✅ Employee Added Successfully!")

    # Search Employee
    elif choice == "3":
        emp_id = int(input("Enter Employee ID to Search: "))

        cursor.execute(
            "SELECT * FROM employees WHERE emp_id=?",
            (emp_id,)
        )

        employee = cursor.fetchone()

        if employee:
            print("\nEmployee Found")
            print(employee)
        else:
            print("❌ Employee Not Found!")

    # Update Employee
    elif choice == "4":
        emp_id = int(input("Enter Employee ID to Update: "))
        salary = float(input("Enter New Salary: "))

        cursor.execute(
            "UPDATE employees SET salary=? WHERE emp_id=?",
            (salary, emp_id)
        )

        conn.commit()
        print("✅ Employee Salary Updated Successfully!")

    # Delete Employee
    elif choice == "5":
        emp_id = int(input("Enter Employee ID to Delete: "))

        cursor.execute(
            "DELETE FROM employees WHERE emp_id=?",
            (emp_id,)
        )

        conn.commit()
        print("✅ Employee Deleted Successfully!")

    # Exit
    elif choice == "6":
        print("🙏 Thank You!")
        break

    else:
        print("❌ Invalid Choice!")

conn.close()
