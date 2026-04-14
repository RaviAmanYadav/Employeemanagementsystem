from app.service.employee_service import add_employee, searchEmployee, showAllEmployee


def run():
    while True:
        print("1. Add employee")
        print("2. Serach Employee")
        print("3. Search All employee.")
        print("4. Exit")
        choice = int(input("Enter your choice => "))
        match choice:
            case 1:
                name = input("Enter Employee name => ")
                age = int(input("Enter Employee age => "))
                position = input("Enter Employee Position => ")
                msg = add_employee(name, age, position)
                print(msg)
            case 2:
                empID = int(input("Enter Emp ID => "))
                msg = searchEmployee(empID)
                for i in msg:
                    print(f"ID : {i["id"]}")
                    print(f"Name : {i["name"]}")
            case 3:
                msg = showAllEmployee()
                for i in msg:
                    print(f"ID : {i["id"]}")
                    print(f"Name : {i["name"]}")
            case 4:
                exit()
