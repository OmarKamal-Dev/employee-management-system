import json
import session
import utils

EmployeeDataFile = "Employee.json"
UsersDataFile    = "Users.json"

def load_users(fileName = UsersDataFile):
    all_users = {}

    with open(fileName, "r") as myFile :
        for line in myFile:
            if line.strip():

                all_users.update(json.loads(line))

    return all_users

def load_employees(fileName=EmployeeDataFile):
    all_employees = {}
    
    with open(fileName, "r") as myFile:
        for line in myFile:
            if line.strip():
                all_employees.update(json.loads(line))
                
    return all_employees

def save_employee(employee, fileName = EmployeeDataFile):
    session.current_session["all_employee"].update(employee)

    with open(fileName, "a") as myFile:
        myFile.write(json.dumps(employee) + "\n")


def update_employees(fileName = EmployeeDataFile):
    
     with open(fileName, "w") as myFile:
        
        for emp_name, emp_data in session.current_session["all_employee"].items():
            
            single_employee = {emp_name: emp_data}
            
            myFile.write(json.dumps(single_employee) + "\n")

def is_employee_exists(employee_name):
    
    if employee_name in session.current_session["all_employee"]:
        return True
    else:
        return False

def print_employee_card(employee_name):
    utils.print_header(employee_name + "'s Card")

    indent = " " * 15

    print(indent + f"Name    : {employee_name}")
    print(indent + f"Age     : {session.current_session["all_employee"][employee_name]["Age"]}")
    print(indent + f"Salary  : {session.current_session["all_employee"][employee_name]["Salary"]}")
    print(indent+  f"Country : {session.current_session["all_employee"][employee_name]["Country"]}")
    
