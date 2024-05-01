## To check python is installed or not

```
where python

or

where.exe python
```

## To create virtual environment

```
python --version

python -m venv venv

Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned

.\venv\Scripts\activate
```

## starting the uvicorn

```
uvicorn main:app --reload
```

## pip install

```
pip install -r requirements.txt
```

## practices followed

- we have feature as single folder and have router, model, schemas, db_repository as classes to communicate with each other.
- router gets the request from the client
- db_repository router class communicates with this class to connect to the db and bring data to the user
- receiving camelCase from frontend and convert to snake_case in python

### ORM library

checklist

- database definition = database.py
- model definition = models.py
- create database = main.py
- schema definition = schemas.py
- ORM functionality = db_user.py
- API functionality = user.py

converts the object oriented code to database model eg SQLALCHEMY.

we are trying to use a timezone when we try to save timestamp so that we can save exactly the time when the user have created or updated the todo.
so we have saved used.

we have moved feature under the corresponding folder and separate it as a separate package.

steps to do are

1: we need to add task inside tasks table
2: we need to add task row under task entry table

need to find the way saving the data in the db.

User Table

One user can have many tasks : One to many relationship(user has one to many relationship with task)
