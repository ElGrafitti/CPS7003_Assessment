from cps7003.cps7003_assessment_2.persistence.cruds.transaction_crud import TransactionCRUD


class TransactionService:
    def __init__(self):
        self.transaction_crud = TransactionCRUD()

    def create_transaction(self, transaction_name):
        return self.transaction_crud.create_transaction(transaction_name)

    def show_all_transactions(self):
        return self.transaction_crud.show_all_transactions()

    def get_transaction_by_id(self, transaction_id):
        return self.transaction_crud.get_transaction_by_id(transaction_id)

    def get_transaction_by_name(self, transaction_name):
        return self.transaction_crud.get_transaction_by_name(transaction_name)

    def update_transaction(self, transaction_id, new_transaction_name):
        return self.transaction_crud.update_transaction(transaction_id, new_transaction_name)

    def delete_transaction(self, transaction_id):
        return self.transaction_crud.delete_transaction(transaction_id)


if __name__ == "__main__":
    transaction_service = TransactionService()
    transaction_service.create_transaction("transact")
