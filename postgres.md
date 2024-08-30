# Connecting to Postgres DB created through docker image

you can use a PostgreSQL Docker image to avoid installing PostgreSQL directly on your machine. Here are the steps to download and run a PostgreSQL Docker container:

- Step1:
  Install Docker: Make sure Docker is installed on your machine. You can download it from Docker's official website.

- Step2:
  Pull the PostgreSQL Docker Image: Use the following command to pull the PostgreSQL image from Docker Hub:

```
docker pull postgres

```

- step3:
  Run the PostgreSQL Container: Use the following command to run a PostgreSQL container:

```
  docker run --name todo_postgres -e POSTGRES_PASSWORD=password -p 5432:5432 -d postgres


--name todo_postgres: Names the container todo_postgres.
-e POSTGRES_PASSWORD=password: Sets the password for the PostgreSQL postgres user.
-d postgres: Runs the container in detached mode using the postgres image.
```

- step4
  Once you create the postgres container you need to create a db which to be done manually but this created automatically in sqllite

Creating the Database:

You may need to create the database mydatabase in PostgreSQL. You can do this by connecting to the PostgreSQL container and running the necessary SQL commands:

Access the PostgreSQL Container:

´´´
docker exec -it todo_postgres psql -U postgres

CREATE DATABASE mydatabase;

\l # list all the databases

\c mydatabase # connect to the database

\dt # list tables

SELECT \* FROM tablename;

-U is the username
´´´

- step5:
  Connect to PostgreSQL: You can connect to the PostgreSQL database using the following connection string in your database.py file:

```
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:password@localhost:5432/todo"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


postgresql://: Specifies the PostgreSQL dialect.
postgres:mysecretpassword: Uses the postgres user with the password mysecretpassword.
@localhost: Connects to the PostgreSQL server running on localhost.
/mydatabase: Specifies the database name (you may need to create this database).

```
