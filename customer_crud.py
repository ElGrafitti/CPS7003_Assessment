from sqlalchemy.orm import sessionmaker
from cps7003.cps7003_assessment_2.persistence.entities.customer import Customer
from cps7003.cps7003_assessment_2.database.stmarysdatatechsolutions import DATABASE_NAME
from sqlalchemy import create_engine


class CustomerCRUD:
    def __init__(self):
        self.engine = create_engine(f'sqlite:///{DATABASE_NAME}')
        self.Session = sessionmaker(bind=self.engine)

    def create_customer(self, first_name, last_name, email, address, mobile_number):
        session = self.Session()
        try:
            customer = {'FirstName': first_name,
                        'LastName': last_name,
                        'Email': email,
                        'Address': address,
                        'MobileNumber': mobile_number}
            new_customer = Customer(**customer)
            session.add(new_customer)
            session.commit()
            return new_customer
        except Exception as e:
            session.rollback()
            print(f"Error creating customer: {e}")
        finally:
            session.close()

    def get_all_customers(self):
        session = self.Session()
        try:
            return session.query(Customer).all()
        finally:
            session.close()

    def get_customers_with_id(self, customer_id):
        session = self.Session()
        try:
            return session.query(Customer).filter_by(CustomerID=customer_id).first()
        finally:
            session.close()

    def get_customer_by_name(self, customer_name):
        session = self.Session()
        try:
            return session.query(Customer).filter_by(CustomerName=customer_name).first()
        finally:
            session.close()

    def update_customer(self, customer_id, new_customer_name):
        session = self.Session()
        try:
            customer = session.query(Customer).filter_by(CustomerID=customer_id).first()
            if Customer:
                customer.CustomerName = new_customer_name
                session.commit()
                return customer
            else:
                return None
        except Exception as e:
            session.rollback()
            print(f"Error updating customer: {e}")
        finally:
            session.close()

    def delete_customer(self, customer_id):
        session = self.Session()
        try:
            customer = session.query(Customer).filter_by(CustomerID=customer_id).first()
            if customer:
                session.delete(customer)
                session.commit()
                return customer
            else:
                return None
        except Exception as e:
            session.rollback()
            print(f"Error deleting customer: {e}")
        finally:
            session.close()
