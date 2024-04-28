CREATE TABLE Account (
    account_id SERIAL PRIMARY KEY,
    customer_id INT UNIQUE REFERENCES Customer(customer_id),
    account_number VARCHAR(20) UNIQUE,
    ifsc_code VARCHAR(15),
    balance DECIMAL(15, 2)
);

CREATE TABLE Customer (
    customer_id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100) UNIQUE
);

CREATE TABLE Transaction (
    transaction_id SERIAL PRIMARY KEY,
    account_id INT REFERENCES Account(account_id),
    amount DECIMAL(10, 2),
    transaction_type VARCHAR(50),
    transaction_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);



CREATE TABLE Customer (
    customer_id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    account_type VARCHAR(50),
    email VARCHAR(100) UNIQUE,
    phone_number VARCHAR(20)
);
CREATE TABLE Card (
    card_id SERIAL PRIMARY KEY,
    customer_id INT REFERENCES Customer(customer_id),
    card_type VARCHAR(20),
    card_number VARCHAR(16) UNIQUE,
    expiry_date DATE,
    cvv VARCHAR(3)
);
CREATE TABLE Transaction (
    transaction_id SERIAL PRIMARY KEY,
    account_id INT REFERENCES Account(account_id),
    transaction_mode VARCHAR(20),
    party_involved VARCHAR(100),
    amount DECIMAL(15, 2),
    transaction_status VARCHAR(20),
    transaction_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE Loan (
    loan_id SERIAL PRIMARY KEY,
    customer_id INT REFERENCES Customer(customer_id),
    loan_type VARCHAR(50),
    amount DECIMAL(15, 2),
    interest_rate DECIMAL(5, 2),
    status VARCHAR(20)
);

CREATE TABLE Insurance (
    insurance_id SERIAL PRIMARY KEY,
    customer_id INT REFERENCES Customer(customer_id),
    insurance_type VARCHAR(50),
    premium DECIMAL(10, 2),
    coverage_amount DECIMAL(15, 2),
    status VARCHAR(20)
);


CREATE TABLE CustomerServicePurchase (
    purchase_id SERIAL PRIMARY KEY,
    customer_id INT REFERENCES Customer(customer_id),
    service_type VARCHAR(50),
    service_id INT,
    purchase_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);




INSERT INTO Customer (name, email) VALUES ('John Doe', 'john.doe@example.com');

INSERT INTO Account (customer_id, balance, account_type) VALUES (1, 1000.00, 'Savings');

INSERT INTO Transaction (account_id, amount, transaction_type) VALUES (1, 500.00, 'Deposit');