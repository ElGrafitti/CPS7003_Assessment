def main_menu():
    menu = """
    St Mary's DataTech Solutions Management System
    ------------------------------------------------------------

    What would you like to do?
    [1] Manage Employees
    [2] Manage Departments
    [3] Manage Customers
    [4] Manage Transactions
    
    Enter selected option: """

    return int(input(menu))


def status(message):
    print(f"Main: {message}")
