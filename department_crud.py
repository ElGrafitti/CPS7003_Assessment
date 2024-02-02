from sqlalchemy.orm import sessionmaker
from cps7003.cps7003_assessment_2.persistence.entities.department import Department
from cps7003.cps7003_assessment_2.database.stmarysdatatechsolutions import DATABASE_NAME
from sqlalchemy import create_engine


class ModuleCRUD:
    def __init__(self):
        self.engine = create_engine(f'sqlite:///{DATABASE_NAME}')
        self.Session = sessionmaker(bind=self.engine)

    def create_department(self, department_name):
        session = self.Session()
        try:
            department = {'DepartmentName': department_name}
            new_department = Department(**department)
            session.add(new_department)
            session.commit()
            return new_department
        except Exception as e:
            session.rollback()
            print(f"Error creating department: {e}")
        finally:
            session.close()

    def get_all_departments(self):
        session = self.Session()
        try:
            return session.query(Department).all()
        finally:
            session.close()

    def get_department_by_id(self, department_id):
        session = self.Session()
        try:
            return session.query(Department).filter_by(DepartmentID=department_id).first()
        finally:
            session.close()

    def get_department_by_name(self, department_name):
        session = self.Session()
        try:
            return session.query(Department).filter_by(Departmentname=department_name).first()
        finally:
            session.close()

    def update_department(self, department_id, new_department_name):
        session = self.Session()
        try:
            department = session.query(Department).filter_by(DepartmentID=department_id).first()
            if department_id:
                department.DepartmentName = new_department_name
                session.commit()
                return department
            else:
                return None
        except Exception as e:
            session.rollback()
            print(f"Error updating department: {e}")
        finally:
            session.close()

    def delete_department(self, department_id):
        session = self.Session()
        try:
            department = session.query(Department).filter_by(DepartmentID=department_id).first()
            if department:
                session.delete(department)
                session.commit()
                return department
            else:
                return None
        except Exception as e:
            session.rollback()
            print(f"Error deleting department: {e}")
        finally:
            session.close()
