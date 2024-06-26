# Banking System Application

This project is the final submission for the Database Course. It is a banking system application developed using SQL for the database schema and Django for the backend application with templates.

# Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Entity Relationship Diagram](#entity-relationship-diagram)
- [Installation](#installation)

- [Usage](#usage)
- [Database Schema](#database-schema)
- [Project Structure](#project-structure)
- [Deployment](#deployment)
- [Technologies Used](#technologies-used)

## Introduction

The Banking System Application is designed to simulate basic banking operations such as managing accounts, transactions, loans, and customer information. It provides a user-friendly interface for both customers and administrators to interact with the system.

## Features

- User authentication and authorization (customer and administrator roles)
- Account management (create, update, delete accounts)
- Transaction processing (deposit, withdrawal, transfer) with atomic transaction logic
- Loan management (apply for loans, view loan status)
- Customer information management (update personal details)

## Entity Relationship Diagram

![Alt text](banking_system_db.png)

## Installation

1. Clone the repository

```bash
git clone https://github.com/muz2002/FinalProject_database.git
```

2. Install the required dependencies:

```bash
cd bank_management
pip install -r requirements.txt
```

3. Set up the database:

- If you want to run the application locally, create a PostgreSQL database and connect the application to that database by configuring the DATABASES setting in settings.py.

4. Apply the migrations to create the necessary tables in the database:

```bash
python manage.py migrate

```

5. Start the Django development server:

```bash
python manage.py runserver

```

6. Access the application in your web browser at http://localhost:8000.

## Usage

- As a customer, you can log in to your account, make transactions to other customer accounts, see for loans, services, transaction history e.t.c .

- As an administrator, you have access to additional features such as managing accounts, viewing transaction logs, creating customers and accounts for them, creating cards, services, loans for your customers.

## Database Schema

The database schema for this application is defined in the table_relations.sql file. It includes tables for accounts, transactions, loans, customers, administrators, and other relevant entities.

## Project Structure

```bash
.
├── README.md
├── bank_app
│   ├── __init__.py
│   ├── __pycache__
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── migrations
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── bank_management
│   ├── __init__.py
│   ├── __pycache__
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
├── requirements.txt
├── static
│   ├── account_styles.css
│   ├── assets
│   ├── back.jpeg
│   └── log_out.webp
├── staticfiles
│   ├── account_styles.css
│   ├── admin
│   ├── assets
│   ├── back.jpeg
│   └── log_out.webp
├── table_relations.sql
├── templates
│   ├── account_detail.html
│   ├── card_detail.html
│   ├── customer_detail.html
│   ├── error.html
│   ├── home.html
│   ├── loan_detail.html
│   ├── login.html
│   ├── logout.html
│   ├── register.html
│   ├── service_purchase_detail.html
│   ├── transaction_detail.html
│   ├── transaction_success.html
│   └── transfer.html
└── user_authentication
    ├── __init__.py
    ├── __pycache__
    ├── admin.py
    ├── apps.py
    ├── forms.py
    ├── migrations
    ├── models.py
    ├── tests.py
    ├── urls.py
    └── views.py
```

## Deployment

The <b>cloud_database</b> which is my main branch of this project is deployed on Render, and you can access it [here](https://banking-system-7g5i.onrender.com) .

To see how the project works locally, switch to <b>development</b>:

```bash
git checkout development
```

## Technologies Used

- SQL for database schema definition
- Django for backend development

- HTML, CSS, and JavaScript for frontend templates
- [Render](https://render.com/) for PostgreSQL database and Django app deployment.

## Contributing

Contributions are welcome! If you find any bugs or have suggestions for improvement, please open an issue or submit a pull request.
