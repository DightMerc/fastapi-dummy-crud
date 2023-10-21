# FastAPI CRUD Project

![Поддерживаемые Python версии](https://img.shields.io/badge/python-3.11+-blue.svg)
[![Лицензия LGPLv3](https://img.shields.io/badge/license-LGPLv3-lightgrey.svg)](https://www.gnu.org/licenses/lgpl-3.0.html)
[![Codacy Badge](https://app.codacy.com/project/badge/Grade/50fd16106eb54631ac687fde2e64cdca)](https://app.codacy.com/gh/DightMerc/fastapi-dummy-crud/dashboard?utm_source=gh&utm_medium=referral&utm_content=&utm_campaign=Badge_grade)

This project is a simple example of a CRUD application built with FastAPI. It demonstrates the basic operations of Create, Read, Update, and Delete (CRUD) using a web API.

## Features

- Utilizes FastAPI to create a fast and reliable API.
- Includes a simple SQLite database for data storage.
- Supports CRUD operations for objects.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/DightMerc/fastapi-dummy-crud.git
    cd fastapi-dummy-crud
    ```

2. Set up environment:

    ```bash
    cp dist.env .env
    ```

3. Init SQLite database:

    ```bash
    cd ./src
    cp template.db app.db
    ```

## Running

Start the application using the following command:

```bash
docker-compose up --build
```

The application will be available at http://localhost:5060.


## Usage

After starting the application, you can use the following endpoints:

### Users

#### Get a List of All Items

Use the following endpoint to retrieve a list of all items:

```http
GET /user
```

#### Create new user

Use the following endpoint to create new user:

```http
POST /user?user_id
```

#### Update user by user_id

Use the following endpoint to update user by its user_id:

```http
PUT /user?user_id
```

#### Delete user by user_id

Use the following endpoint to delete user by its user_id:

```http
DELETE /user?user_id
```


### Auth

#### Login

Use the following endpoint for login via username & password:

```http
POST /auth/login
```


#### Sign Up

Use the following endpoint for sign up via username & password:

```http
POST /auth/signup
```

## Documentation

Based on SwaggerIO documentation engine:

http://localhost:5060/docs
