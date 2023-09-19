# TrueCallerApi

A Django based application that can be used to detect and report spam callers.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Authentication](#authentication)
- [Endpoints](#endpoints)
  - [Users](#users)
    - [Get All Users](#get-all-users)
    - [Create a User](#create-a-user)
    - [Login](#login)
  - [Contacts](#contacts)
    - [All Contacts](#all-contacts)
    - [Create Contact](#create-contact)
  - [Spam Reports](#spam-reports)
    - [All Spam Reports](#all-spam-reports)
    - [Create Spam Report](#create-spam-report)
  - [Search](#search)
- [Contributing](#contributing)
- [License](#license)

## Installation

To begin, make sure you have Python installed on your computer.

1. Create and Activate a virtual environment using `venv`.
2. Move to the project directory and run the command `pip install -r requirements.txt`.
3. Run the command `python manage.py runserver`. You can copy the address from the terminal.
4. Open the address copied from the terminal on a browser.

## Usage

Due to the security permissions, you need to be signed in to access the endpoints.

### For Browsers:

1. Go to [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin).
2. Login with the credentials:
   - Phone: 9815775735
   - Password: 12345678
3. Now you can access all the endpoints.

### For Services like Postman:

1. Create a user from the relevant endpoint mentioned below.
2. Login with credentials you just created and copy the token that you receive.
3. Put `Authorization: Token {your_token}` in the header for subsequent requests.

## Authentication

For services like Postman, you need to create a user, log in with the credentials, and use the received token with subsequent requests.

## Endpoints

### Users

#### Get All Users

- Endpoint: [http://127.0.0.1:8000/users/](http://127.0.0.1:8000/users/)
- Method: GET
- Json Format: Get Request with the token header

#### Create a User

- Endpoint: [http://127.0.0.1:8000/users/create/](http://127.0.0.1:8000/users/create/)
- Method: POST
- Json Format:

```json
{
  "name": "",
  "phone": "",
  "password": "",
  "email": "" // optional
}
```

### Login

- **Endpoint:** [http://127.0.0.1:8000/users/login/](http://127.0.0.1:8000/users/login/)
- **Method:** POST
- **Json Format:**

```json
{
  "username": "", // phone you registered with
  "password": ""
}
```

### Contacts

#### All Contacts

- **Endpoint:** [http://127.0.0.1:8000/contacts/](http://127.0.0.1:8000/contacts/)
- **Method:** GET
- **Json Format:** Get Request

#### Create Contact

- **Endpoint:** [http://127.0.0.1:8000/contacts/create](http://127.0.0.1:8000/contacts/create)
- **Method:** POST
- **Json Format:**

```json
{
  "name": "",
  "email": "", // optional
  "phone": ""
}
```

### Spam Reports

#### All Spam Reports

- **Endpoint:** [http://127.0.0.1:8000/spam/](http://127.0.0.1:8000/spam/)
- **Method:** GET
- **Json Format:** Get Request

#### Create Spam Report

- **Endpoint:** [http://127.0.0.1:8000/spam/report/](http://127.0.0.1:8000/spam/report/)
- **Method:** POST
- **Json Format:**

```json
{
  "name": "",
  "phone": "" // number to report for spamming
}
```

### Search

#### Search people or contacts

- **Endpoint:** [http://127.0.0.1:8000/search/](http://127.0.0.1:8000/search/)
- **Method:** POST
- **Json Format:**

```json
{
  "query": "" // either the phone number or the name of the contact or user
}
```


