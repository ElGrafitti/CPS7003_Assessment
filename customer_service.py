from cps7003.cps7003_assessment_2.persistence.cruds.customer_crud import CustomerCRUD


class CustomerService:
    def __init__(self):
        self.customer_crud = CustomerCRUD()

    def create_customer(self, first_name, last_name, email, address, mobile_number):
        return self.customer_crud.create_customer(first_name, last_name, email, address, mobile_number)

    def get_all_customers(self):
        return self.customer_crud.get_all_customers()

    def get_customer_by_id(self, customer_id):
        return self.customer_crud.get_customers_with_id(customer_id)

    def get_customer_by_name(self, customer_name):
        return self.customer_crud.get_customer_by_name(customer_name)

    def update_customer(self, customer_id, new_customer_name):
        return self.customer_crud.update_customer(customer_id, new_customer_name)

    def delete_customer(self, customer_id):
        return self.customer_crud.delete_customer(customer_id)


if __name__ == "__main__":
    customer_service = CustomerService()
    customer_service.create_customer("first_name", "last_name", "email", "address", "mobile_number")
