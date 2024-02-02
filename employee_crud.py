
from sqlalchemy.orm import sessionmaker
from cps7003.cps7003_assessment_2.persistence.entities.employee import Employee
from cps7003.cps7003_assessment_2.database.stmarysdatatechsolutions import DATABASE_NAME
from sqlalchemy import create_engine


class EmployeeCRUD:
    def __init__(self):
        self.engine = create_engine(f'sqlite:///{DATABASE_NAME}')
        self.Session = sessionmaker(bind=self.engine)

    def create_employee(self, first_name, last_name, email, dob, mobile_number, address):
        session = self.Session()
        try:
            employee = {'FirstName': first_name, 'LastName': last_name, 'Email': email, 'DOB': dob, 'MobileNumber': mobile_number, 'Address': address}

            new_employee = Employee(**employee)
            session.add(new_employee)
            session.commit()
            return new_employee
        except Exception as e:
            session.rollback()
            print(f"Error creating Employee: {e}")
        finally:
            session.close()

    def get_all_employees(self):
        session = self.Session()
        try:
            return session.query(Employee).all()
        finally:
            session.close()

    def get_employee_by_id(self, employee_id):
        session = self.Session()
        try:
            return session.query(Employee).filter_by(EmployeeID=employee_id).first()
        finally:
            session.close()

    def get_employee_by_name(self, employee_name):
        session = self.Session()
        try:
            return session.query(Employee).filter_by(EmployeeName=employee_name).first()
        finally:
            session.close()

    def update_employee(self, employee_id, new_employee_name):
        session = self.Session()
        try:
            employee = session.query(Employee).filter_by(EmployeeID=employee_id).first()
            if employee:
                employee.EmployeeName = new_employee_name
                session.commit()
                return employee
            else:
                return None
        except Exception as e:
            session.rollback()
            print(f"Error updating employee: {e}")
        finally:
            session.close()

    def delete_employee(self, employee_id):
        session = self.Session()
        try:
            employee = session.query(Employee).filter_by(EmployeeID=employee_id).first()
            if employee:
                session.delete(employee)
                session.commit()
                return employee
            else:
                return None
        except Exception as e:
            session.rollback()
            print(f"Error deleting employee: {e}")
        finally:
            session.close()
