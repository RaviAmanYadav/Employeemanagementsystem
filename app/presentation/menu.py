from app.service.employee_service import add_Employee


def run():
    while True:
        print("1.Add employee")
        print("2. Exit")
        choice = int(input("Enter your choice => "))
        match choice:
            case 1:
                name = input("Enter Employee name => ")
                age = int(input("Enter Employee age => "))
                position = input("Enter Employee Position => ")
                msg = add_Employee(name, age, position)
                print(msg)
            case 2:
                exit()
