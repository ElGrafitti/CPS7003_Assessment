from cps7003.cps7003_assessment_2.tui import main_tui, employee_tui, department_tui, customer_tui, transaction_tui
from cps7003.cps7003_assessment_2.services.employee_service import EmployeeService
from cps7003.cps7003_assessment_2.services.department_service import DepartmentService
from cps7003.cps7003_assessment_2.services.customer_service import CustomerService
from cps7003.cps7003_assessment_2.services.transaction_service import TransactionService


def employee_system():
    employee_service = EmployeeService()

    selected = employee_tui.employee_menu()

    if selected == 1:
        employee_details = employee_tui.employee_details()
        created_employee = employee_service.create_employee(first_name=employee_details.employee.FirstName,
                                                            last_name=employee_details.employee.LastName,
                                                            email=employee_details.employee.Email,
                                                            dob=employee_details.employee.DOB,
                                                            mobile_number=employee_details.employee.MobileNumber,
                                                            address=employee_details.employee.Address)
        if created_employee:
            employee_tui.status(f"The {employee_details} role has been created.")
        else:
            employee_tui.status(f"The {employee_details} could not be created.")

    elif selected == 2:
        find_employee = employee_tui.find_employee_by_id()
        employee = employee_service.get_employee_by_id(find_employee)
        if employee:
            employee_tui.status(f"The {employee} Department exists in the database.")
        else:
            employee_tui.status(f"The {employee} Department could not be found.")

    elif selected == 3:
        employee_update = employee_tui.update_employee()
        updated_employee = employee_service.update_employee(employee_id=employee_update,
                                                            new_employee_name=employee_update)
        if updated_employee:
            employee_tui.status(f"The {updated_employee} Employee has been updated successfully.")
        else:
            employee_tui.status(f"The {updated_employee} Employee update failed.")

    elif selected == 4:


    else:
        employee_tui.status("Invalid role action.")


def department_system():
    department_service = DepartmentService()

    selected = department_tui.department_menu()

    if selected == 1:
        department_name = department_tui.department_details()
        created_department = department_service.create_department(department_name=department_name)
        if created_department:
            department_tui.status(f"The {department_name} Department has been created.")
        else:
            department_tui.status(f"The {department_name} Department could not be created.")
    elif selected == 2:
        department_name = input("Please input the name of the department to look up: ")
        find_department = department_service.get_department_by_name(department_name)
        if find_department is True:
            department_tui.status(f"The {department_name} Department exists in the database.")
        else:
            department_tui.status(f"The {department_name} Department could not be found.")

    elif selected == 3:
        new_department_name = department_tui.update_department_details()
        department_update = department_service.update_department(department_id=new_department_name.DepartmentID,
                                                                 new_department_name=new_department_name)
        if department_update:
            department_tui.status(f"The {new_department_name} Department has been updated successfully.")
        else:
            department_tui.status(f"The {department_update} Department update failed.")

    elif selected == 4:
        department_to_delete = department_tui.delete_department()
        department_delete = department_service.delete_department(department_id=department_to_delete)
        if department_delete:
            department_tui.status(f"The {department_delete.DepartmentName} Department has been updated successfully.")
        else:
            department_tui.status(f"The {department_delete.DepartmentName} Department failed to delete.")

    else:
        department_tui.status("Invalid role action.")


def customer_system():
    customer_service = CustomerService()

    selected = customer_tui.customer_menu()

    if selected == 1:
        customer_details = customer_tui.customer_details()
        created_customer = customer_service.create_customer(first_name=customer_details.customer.FirstName,
                                                            last_name=customer_details.FirstName,
                                                            email=customer_details.Email,
                                                            mobile_number=customer_details.MobileNumber,
                                                            address=customer_details.Address)
        if created_customer:
            customer_tui.status(f"The {customer_details} has been created.")
        else:
            customer_tui.status(f"The {customer_details} could not be created.")
    else:
        customer_tui.status("Invalid role action.")


def transaction_system():
    transaction_service = TransactionService()

    selected = transaction_tui.transaction_menu()

    if selected == 1:
        transaction_name = transaction_tui.transaction_details()
        created_transaction = transaction_service.create_transaction(transaction_name)
        if created_transaction:
            transaction_tui.status(f"The {transaction_name} has been added the system.")
        else:
            transaction_tui.status(f"The {transaction_name} could not be generated.")
    else:
        transaction_tui.status("Invalid role action.")


def run():
    while True:

        selected = main_tui.main_menu()

        if selected == 1:
            employee_system()

        elif selected == 2:
            department_system()

        elif selected == 3:
            customer_system()

        elif selected == 4:
            transaction_system()

        else:
            main_tui.status("Invalid menu action.")


if __name__ == "__main__":
    run()
