import utils
import session
import dp

def add_employee():
    add_more = 'y'

    while(add_more == 'y' or add_more == 'Y'):
        utils.clear_screen()

        utils.print_header("Add Employee Screen")

        user_name = input("Enter Employee User Name: ")
        age       = input("Enter Employee Age      : ")
        salary    = input("Enter Employee Salary   : ")                                                       
        country   = input("Enter Employee Country  : ")

        dp.save_employee({user_name : {
            "Age"    : age,
            "Salary" : salary,
            "Country": country
        }})

        print("Employee Added Successfully.")
        add_more = input("Do You Want To Add More?(Y or N) ")
    
    return

def update_employee():
    update_more = 'y'

    while(update_more == 'y' or update_more == 'Y'):
        utils.clear_screen()

        utils.print_header("Update Employee Screen")
        
        employee_name = input("Enter Employee Name: ")

        while(not dp.is_employee_exists(employee_name)):
            print("Invalid Name Please Try Again.")

            employee_name = input("Enter Employee Name: ")
        
        print("Employee Found Successfully, Here Is His Card")
        dp.print_employee_card(employee_name)

        newName = input("Enter New Employee Name   : ")
        age     = input("Enter New Employee Age    : ")
        salary  = input("Enter New Employee Salary : ")
        country = input("Enter New Employee Country: ")

        session.current_session["all_employee"][newName]            = session.current_session["all_employee"].pop(employee_name)
        session.current_session["all_employee"][newName]["Age"]     = age
        session.current_session["all_employee"][newName]["Salary"]  = salary
        session.current_session["all_employee"][newName]["Country"] = country

        dp.update_employees()

        print("Employee Updated Successfully.")
        
        update_more = input("Do You Want To Update More?(Y or N) ")

    return

    

def delete_employee():
    delete_more = 'y'

    while(delete_more == 'y' or delete_more == 'Y'):
        utils.clear_screen()

        utils.print_header("Delete Employee Screen")
        
        employee_name = input("Enter Employee Name: ")

        while(not dp.is_employee_exists(employee_name)):
            print("Invalid Name Please Try Again.")

            employee_name = input("Enter Employee Name: ")
        
        print("Employee Found Successfully, Here Is His Card")
        dp.print_employee_card(employee_name)

        confirmation = input("Are You Sure You Want to Delete This Employee? (Y or N)")

        if confirmation.lower() == 'y':
            del session.current_session["all_employee"][employee_name]

            dp.update_employees()

            print("Employee Deleted Successfully.")

        else:
            input("Nothing Happend, Press Enter To Return...")
            
            return

        delete_more = input("Do You Want To Update More?(Y or N) ")

    return 

def search_employee():
    search_more = 'y'

    while(search_more == 'y' or search_more == 'Y'):
        utils.clear_screen()

        utils.print_header("Search Employee Screen")
        
        employee_name = input("Enter Employee Name: ")

        while(not dp.is_employee_exists(employee_name)):
            print("Invalid Name Please Try Again.")

            employee_name = input("Enter Employee Name: ")
        
        print("Employee Found Successfully, Here Is His Card")
        dp.print_employee_card(employee_name)

        delete_more = input("Do You Want To Search More?(Y or N) ")

    return 

def print_employee_List():
    utils.clear_screen()
    
    for name, value in session.current_session["all_employee"].items():
        print(f"Name : {name} - Age : {value["Age"]} - Salary : {value["Salary"]} - Country : {value["Country"]}")

    input("Press Enter To Return...")
    

def main_menu():
    while(True):
        utils.clear_screen()
        
        utils.print_header("Main Menu Screen")

        indent = " " * 15

        print(indent + "[1] Add Employee\n")
        print(indent + "[2] Update Employee\n")
        print(indent + "[3] Delete Employee\n")
        print(indent + "[4] Search Employee\n")
        print(indent + "[5] Print Employee List\n")
        print(indent + "[6] Log out\n")

        choose = utils.read_int_in_range(1,6)

        match choose:
            case 1:
                add_employee()
            case 2:
                update_employee()
            case 3:
                delete_employee()
            case 4:
                search_employee()
            case 5: 
                print_employee_List()
            case 6:
                session.current_session["all_users"]    = dict()
                session.current_session["all_employee"] = dict()
                session.current_session["username"]     = None
                return

def log_in():
    while(True):
        utils.clear_screen()

        session.current_session["all_users"]    = dp.load_users()
        session.current_session["all_employee"] = dp.load_employees()

        utils.print_header("L O G   I N")

        userName = utils.check_user()
        password = False
        tries = 3

        while(not password and tries > 0):
            print(f"You Have {tries} trie(s) Left.")

            password = utils.check_password(userName)

            tries -= 1
        
        if password :
            session.current_session["username"] = userName
            
            main_menu()
        else:
            return

def main():
    log_in()

if __name__ == "__main__":
    main()

    
    

    






