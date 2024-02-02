def customer_menu():
    menu = """
    St Mary's DataTech Solutions Management System - Customers
    ------------------------------------------------------------

    What would you like to do?
    [1] Add a new Customer
    [2] Find an existing Customer
    [3] Update an existing Customer
    [4] Delete an existing Customer

    Enter selected option: """

    return int(input(menu))


def customer_details():
    print("Please fill in the details of new Customer")
    return (input("Please enter the First name: "),
            input("Please enter the Last name: "),
            input("Please enter Email: "),
            input("Please enter Mobile Number: "),
            input("Please enter Address"))


def status(message):
    print(f"Personal Details: {message}")
