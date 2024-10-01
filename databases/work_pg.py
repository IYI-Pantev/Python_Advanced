import psycopg2
# import getpass
# import os

# print(os.path.dirname(psycopg2.__file__))

# connect to postgresql
# password = getpass.getpass(prompt='Enter your PostgreSQL password: ')

conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password='iw811',
    host="localhost",
    port="5432"
)

cursor = conn.cursor()

# do smth
cursor.execute(
    """CREATE TABLE IF NOT EXISTS users (
        user_id SERIAL PRIMARY KEY,
        username VARCHAR(50) NOT NULL,
        age INT NOT NULL,
        password VARCHAR(50) NOT NULL
    );
    """
)

# cursor.execute(
#     """INSERT INTO users (username, age, password) VALUES
#     ('johndoe', 30, 'qwerty'),
#     ('alexpn', 25, 'password');
#     """
# )

cursor.execute(
    """SELECT * FROM users;"""
)
print(cursor.fetchall())

# commit the sql query
conn.commit()


# after done
cursor.close()
conn.close()
