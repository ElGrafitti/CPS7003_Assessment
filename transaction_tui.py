def transaction_menu():
    menu = """
    St Mary's DataTech Solutions Management System - Transactions
    ------------------------------------------------------------

    What would you like to do?
    [1] Initiate a new Transaction
    [2] Find an existing Transaction
    [3] Update an existing Transaction
    [4] Delete an existing Transaction

    Enter selected option: """

    return int(input(menu))


def transaction_details():
    print("Please fill in the details of the transactions you wish to initiate")
    return input("Please enter the Transaction name: ")


def status(message):
    print(f"Personal Details: {message}")