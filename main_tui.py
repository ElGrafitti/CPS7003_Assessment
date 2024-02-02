def main_menu():
    menu = """
    St Mary's DataTech Solutions Management System
    ------------------------------------------------------------

    What would you like to do?
    [1] Manage Employees
    [2] Manage Users
    
    Enter selected option: """

    return int(input(menu))


def status(message):
    print(f"Main: {message}")
