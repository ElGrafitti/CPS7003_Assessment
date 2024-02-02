from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Transaction(Base):
    __tablename__ = "Transaction"
    TransactionID = Column(Integer, primary_key=True, autoincrement=True)
    TransactionName = Column(String, unique=True, nullable=False)
    PaymentType = Column(String, nullable=False)
    PaymentDate = Column(String, nullable=False)
    CustomerID = Column(Integer, ForeignKey("Customer.CustomerID", ondelete="CASCADE"), nullable=False)
