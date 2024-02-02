import sqlalchemy as db
from cps7003.cps7003_assessment_2.database.stmarysdatatechsolutions import DATABASE_NAME

# create database engine
engine = db.create_engine(f"sqlite:///{DATABASE_NAME}")
conn = engine.connect()
meta_data = db.MetaData()

# use the database engine
employee_table = db.Table("Employee", meta_data,
                          db.Column("EmployeeID", db.Integer(), primary_key=True, autoincrement=True),
                          db.Column("FirstName", db.String(), nullable=False),
                          db.Column("LastName", db.String(), nullable=False),
                          db.Column("Email", db.String(), nullable=False),
                          db.Column("DOB", db.String(), nullable=False),
                          db.Column("MobileNumber", db.Integer(), nullable=False),
                          db.Column("Address", db.String(), nullable=False),
                          db.Column("DepartmentID", db.Integer(), db.ForeignKey("Department.DepartmentID", ondelete="CASCADE"),
                                    nullable=False))


customer_table = db.Table("Customer", meta_data,
                          db.Column("CustomerID", db.Integer(), primary_key=True, autoincrement=True),
                          db.Column("FirstName", db.String(), nullable=False),
                          db.Column("LastName", db.String(), nullable=False),
                          db.Column("MobileNumber", db.Integer(), nullable=False),
                          db.Column("Email", db.String(), nullable=False))


department_table = db.Table("Department", meta_data,
                            db.Column("DepartmentID", db.Integer(), primary_key=True, autoincrement=True),
                            db.Column("DepartmentName", db.String(), nullable=False))

transaction_table = db.Table("Transaction", meta_data,
                             db.Column("TransactionID", db.Integer(), primary_key=True, autoincrement=True),
                             db.Column("TransactionName", db.String(), nullable=False),
                             db.Column("TransactionType", db.String(), nullable=False),
                             db.Column("TransactionDate", db.String(), nullable=False),
                             db.Column("MobileNumber", db.Integer(), nullable=False),
                             db.Column("CustomerID", db.Integer(), db.ForeignKey("Customer.CustomerID", ondelete="CASCADE"),
                                       nullable=False))

# Go ahead and create the database
meta_data.create_all(engine)
