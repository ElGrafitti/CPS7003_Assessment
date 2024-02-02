def department_menu():
    menu = """
    St Mary's DataTech Solutions Management System - Department
    ------------------------------------------------------------

    What would you like to do?
    [1] Add a new Department
    [2] Find an existing Department
    [3] Update an existing Department
    [4] Delete an existing Department

    Enter selected option: """

    return int(input(menu))


def department_details():
    print("Please fill in the details of the Department you wish to create")
    return input("Please enter the Department name: ")


def update_department_details():
    print("Please fill Department ID")
    return input("Department ID")


def delete_department():
    print("Which department do you want to delete?")
    return input("Department ID: ")


def status(message):
    print(f"Department Details: {message}")
