CREATE DATABASE banking_db;
USE banking_db;
SELECT DATABASE();
CREATE TABLE customers (
    customer_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name  VARCHAR(50) NOT NULL,
    last_name   VARCHAR(50) NOT NULL,
    phone       VARCHAR(15),
    email       VARCHAR(100),
    date_of_birth DATE,
    street_no   VARCHAR(50),
    city        VARCHAR(50),
    state       VARCHAR(50),
    pincode     VARCHAR(10),
    created_at  TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE accounts (
    account_id   INT AUTO_INCREMENT PRIMARY KEY,
    customer_id  INT NOT NULL,
    account_type VARCHAR(20),
    balance      DECIMAL(12,2) CHECK (balance >= 0),
    status       VARCHAR(20),
    created_at   TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);


CREATE TABLE transactions (
    txn_id        INT AUTO_INCREMENT PRIMARY KEY,
    from_account  INT NOT NULL,
    to_account    INT NOT NULL,
    amount        DECIMAL(12,2) CHECK (amount > 0),
    status        VARCHAR(20),
    created_at    TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (from_account) REFERENCES accounts(account_id),
    FOREIGN KEY (to_account)   REFERENCES accounts(account_id),
    CHECK (from_account <> to_account)
);

CREATE TABLE transaction_audit (
    audit_id     INT AUTO_INCREMENT,
    txn_id       INT NOT NULL,
    action       VARCHAR(50),
    remarks      VARCHAR(255),
    performed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (audit_id, txn_id),
    FOREIGN KEY (txn_id) REFERENCES transactions(txn_id)
);

SHOW TABLES;

INSERT INTO customers
(first_name, last_name, phone, email, date_of_birth)
VALUES
('Rahul', 'Sharma', '9876543210', 'rahul@gmail.com', '1998-05-10'),
('Anita', 'Verma', '9123456789', 'anita@gmail.com', '1997-03-22');

INSERT INTO accounts
(customer_id, account_type, balance, status)
VALUES
(1, 'SAVINGS', 5000, 'ACTIVE'),
(2, 'SAVINGS', 3000, 'ACTIVE');


SELECT * FROM customers;
SELECT * FROM accounts;


START TRANSACTION;

-- Check balance
SELECT balance FROM accounts WHERE account_id = 1 FOR UPDATE;

-- Debit sender
UPDATE accounts
SET balance = balance - 1000
WHERE account_id = 1;

-- Credit receiver
UPDATE accounts
SET balance = balance + 1000
WHERE account_id = 2;

-- Insert transaction record
INSERT INTO transactions
(from_account, to_account, amount, status)
VALUES (1, 2, 1000, 'SUCCESS');

COMMIT;

START TRANSACTION;

UPDATE accounts SET balance = balance - 10000 WHERE account_id = 1;

-- Force rollback
ROLLBACK;

SELECT balance FROM accounts WHERE account_id = 1;

INSERT INTO transaction_audit
(txn_id, action, remarks)
VALUES
(1, 'TRANSFER', 'Money transferred successfully');


CREATE VIEW transaction_history AS
SELECT
    txn_id,
    from_account,
    to_account,
    amount,
    status,
    created_at
FROM transactions;




SELECT * FROM transaction_history;


START TRANSACTION;

UPDATE accounts
SET balance = balance - 10000
WHERE account_id = 1;

-- if error occurs
ROLLBACK;


INSERT INTO transactions
(from_account, to_account, amount, status)
VALUES (1, 2, 10000, 'FAILED');


INSERT INTO transaction_audit
(txn_id, action, remarks)
VALUES (LAST_INSERT_ID(), 'TRANSFER_FAILED', 'Insufficient balance');


ALTER TABLE transactions
MODIFY from_account INT NULL,
MODIFY to_account INT NULL,
ADD COLUMN txn_type VARCHAR(20);


UPDATE accounts SET status = 'BLOCKED' WHERE account_id = 2;
UPDATE accounts SET status = 'ACTIVE' WHERE account_id = 2;
