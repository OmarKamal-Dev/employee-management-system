import session
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def print_header(head) -> str:
    print("#" * 50)
    print(head.center(50))
    print("#" * 50)

def read_int(msg) -> int:
    while True:
        try:
            return int(input(msg))
        except ValueError:
            print("Invalid Number Please Try Again.")
    
    return int(number)
    
def read_int_in_range(fromNum, toNum) -> int :
    number = int(read_int(f"Please Enter Number Between {fromNum} and {toNum}: "))

    while(number < fromNum or number > toNum):
        print(f"Invalid Number Please Enter Number Between {fromNum} and {toNum}.")

        number = int(read_int(f"Please Enter Number Between {fromNum} and {toNum}: "))

    return number


def check_user() -> dict:

    while(True):
        userName = input("Please Enter Your User Name : ")

        if userName in session.current_session["all_users"]:
            return userName
        else:
            print("User Name Not Found Please Try Again.")    

def check_password(userName):
        password = input("Please Enter Your Password : ")

        if password == session.current_session["all_users"][userName]:
            return True
        else:
            print("Password Incorrect Please Try Again.")
    
