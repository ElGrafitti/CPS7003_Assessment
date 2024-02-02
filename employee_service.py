from cps7003.cps7003_assessment_2.persistence.cruds.employee_crud import EmployeeCRUD


class EmployeeService:
    def __init__(self):
        self.employee_crud = EmployeeCRUD()

    def create_employee(self, first_name, last_name, email, dob, mobile_number, address):
        return self.employee_crud.create_employee(first_name, last_name, email, dob, mobile_number, address)

    def get_all_employees(self):
        return self.employee_crud.get_all_employees()

    def get_employee_by_id(self, employee_id):
        return self.employee_crud.get_employee_by_id(employee_id)

    def get_employee_by_name(self, employee_name):
        return self.employee_crud.get_employee_by_name(employee_name)

    def update_employee(self, employee_id, new_employee_name):
        return self.employee_crud.update_employee(employee_id, new_employee_name)

    def delete_employee(self, employee_id):
        return self.employee_crud.delete_employee(employee_id)


if __name__ == "__main__":
    employee_service = EmployeeService()
    employee_service.create_employee("first_name", "last_name", "email", "DOB", "mobile_number", "Address")
