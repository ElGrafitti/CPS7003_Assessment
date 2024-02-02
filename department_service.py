from cps7003.cps7003_assessment_2.persistence.cruds.department_crud import DepartmentCRUD


class DepartmentService:
    def __init__(self):
        self.department_crud = DepartmentCRUD()

    def create_department(self, department_name):
        return self.department_crud.create_department(department_name)

    def get_all_departments(self):
        return self.department_crud.get_all_departments()

    def get_department_by_id(self, department_id):
        return self.department_crud.get_department_by_id(department_id)

    def get_department_by_name(self, department_name):
        return self.department_crud.get_department_by_name(department_name)

    def update_department(self, department_id, new_department_name):
        return self.department_crud.update_department(department_id, new_department_name)

    def delete_department(self, department_id):
        return self.department_crud.delete_department(department_id)


if __name__ == "__main__":
    department_service = DepartmentService()
    department_service.create_department("IT")
