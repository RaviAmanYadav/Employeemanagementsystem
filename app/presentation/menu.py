from app.service.employee_service import (
    add_employee,
    searchEmployee,
    showAllEmployee,
    deleteEmployee,
    updateEmployee,
)


def run():
    while True:
        print("1. Add employee")
        print("2. Serach Employee")
        print("3. Search All employee.")
        print("4. Delete Employee")
        print("5. Update Employee")
        print("6. Exit")
        choice = int(input("Enter your choice => "))
        match choice:
            case 1:
                print("*" * 10)
                print("Add Employee")
                name = input("Enter Employee name => ")
                age = int(input("Enter Employee age => "))
                position = input("Enter Employee Position => ")
                msg = add_employee(name, age, position)
                print(msg)
            case 2:
                print("*" * 10)
                print("Search Employee using ID")
                empID = int(input("Enter Emp ID => "))
                msg = searchEmployee(empID)
                for i in msg:
                    print(f"ID : {i["id"]}")
                    print(f"Name : {i["name"]}")
            case 3:
                print("*" * 10)
                print("All employee result")
                msg = showAllEmployee()
                for i in msg:
                    print(f"ID : {i["id"]}")
                    print(f"Name : {i["name"]}")
            case 4:
                print("*" * 10)
                print("Deletion of employee")
                empID = int(input("Enter the employee id => "))
                msg = deleteEmployee(empID)
                print(msg)
            case 5:
                print("*" * 10)
                print("Updating employee")
                empID = int(input("Enter Employee id => "))
                msg = updateEmployee(empID)
                print(msg)
            case 6:
                exit()
