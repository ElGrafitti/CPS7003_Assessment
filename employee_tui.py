def employee_menu():
    menu = """
    St Mary's DataTech Solutions Management System - Employee
    ------------------------------------------------------------

    What would you like to do?
    [1] Add a new Employee
    [2] Find an existing Employee
    [3] Update an existing Employee
    [4] Delete an existing Employee

    Enter selected option: """

    return int(input(menu))


def employee_details():
    print("Please fill in the details of new Employee")
    return input("Please enter the First name: "), input("Please enter the Last name: "), input("Please enter Email: "), input("Please enter Mobile Number: "), input("Please enter Date of Birth: ")


def status(message):
    print(f"Personal Details: {message}")
