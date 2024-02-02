CREATE TABLE IF NOT EXISTS Employee (
    EmployeeID   INTEGER PRIMARY KEY AUTOINCREMENT
                         UNIQUE
                         NOT NULL,
    EmployeeFirstName    TEXT    UNIQUE
                         NOT NULL,
    EmployeeLastName     TEXT    UNIQUE
                         NOT NULL,
    Email        TEXT    UNIQUE
                         NOT NULL,
    MobileNumber INTEGER UNIQUE
                         NOT NULL,
    DOB          TEXT    NOT NULL,
    DepartmentID INTEGER REFERENCES Department (DepartmentID)
                         NOT NULL
                         UNIQUE
);

CREATE TABLE IF NOT EXISTS Department (
    DepartmentID INTEGER PRIMARY KEY AUTOINCREMENT
                       UNIQUE
                       NOT NULL
);

CREATE TABLE IF NOT EXISTS Customer (
    CustomerID        INTEGER PRIMARY KEY AUTOINCREMENT
                              UNIQUE
                              NOT NULL,
    CustomerFirstName TEXT    UNIQUE
                              NOT NULL,
    CustomerLastName  TEXT    UNIQUE
                              NOT NULL,
    Email             TEXT    NOT NULL
                              UNIQUE,
    Address           TEXT,
    MobileNumber      INTEGER NOT NULL
                              UNIQUE
);

CREATE TABLE [Transaction] (
    TransactionID INTEGER PRIMARY KEY AUTOINCREMENT
                          UNIQUE
                          NOT NULL,
    PaymentType   TEXT    NOT NULL,
    PaymentDate   TEXT    NOT NULL,
    CustomerID    INTEGER REFERENCES Customer (CustomerID)
                          NOT NULL
);
