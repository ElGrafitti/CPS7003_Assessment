from sqlalchemy.orm import sessionmaker
from cps7003.cps7003_assessment_2.persistence.entities.transaction import Transaction
from cps7003.cps7003_assessment_2.database.stmarysdatatechsolutions import DATABASE_NAME
from sqlalchemy import create_engine


class TransactionCRUD:
    def __init__(self):
        self.engine = create_engine(f'sqlite:///{DATABASE_NAME}')
        self.Session = sessionmaker(bind=self.engine)

    def create_transaction(self, transaction_name):
        session = self.Session()
        try:
            transaction = {'Transaction': transaction_name}
            new_transaction = Transaction(**transaction)
            session.add(new_transaction)
            session.commit()
            return new_transaction
        except Exception as e:
            session.rollback()
            print(f"Error creating transaction: {e}")
        finally:
            session.close()

    def get_all_transactions(self):
        session = self.Session()
        try:
            return session.query(Transaction).all()
        finally:
            session.close()

    def get_transaction_by_id(self, transaction_id):
        session = self.Session()
        try:
            return session.query(Transaction).filter_by(TransactionID=transaction_id).first()
        finally:
            session.close()

    def get_transaction_by_name(self, transaction_name):
        session = self.Session()
        try:
            return session.query(Transaction).filter_by(TransactionName=transaction_name).first()
        finally:
            session.close()

    def update_transaction(self, transaction_id, new_transaction_name):
        session = self.Session()
        try:
            transaction = session.query(Transaction).filter_by(TransactionID=transaction_id).first()
            if transaction:
                transaction.TransactionName = new_transaction_name
                session.commit()
                return transaction
            else:
                return None
        except Exception as e:
            session.rollback()
            print(f"Error updating transaction: {e}")
        finally:
            session.close()

    def delete_transaction(self, transaction_id):
        session = self.Session()
        try:
            transaction = session.query(Transaction).filter_by(TransactionID=transaction_id).first()
            if transaction:
                session.delete(transaction)
                session.commit()
                return transaction
            else:
                return None
        except Exception as e:
            session.rollback()
            print(f"Error deleting transaction: {e}")
        finally:
            session.close()
