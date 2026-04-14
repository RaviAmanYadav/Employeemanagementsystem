from app.repository.employee_repo import read_data, write_data
from app.models.employee import Employee
from app.utils.helpers import generate_id


def add_employee(name, age, positon):
    employees = read_data()

    emp = Employee(id=generate_id(employees), name=name, age=age, position=positon)

    employees.append(emp.to_dict())
    write_data(employees)
    return "Employee Successfully Added"


def searchEmployee(id):
    employee = read_data()

    result = []
    for emp in employee:
        if emp["id"] == id:
            result.append(emp)

    return result
    