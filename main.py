from dotenv import load_dotenv, find_dotenv
import os
import mysql.connector

load_dotenv(find_dotenv())

HOST = os.environ.get('HOST')
USER = os.environ.get('USER')
PASSWORD = os.environ.get('PASSWORD')
DATABASE = os.environ.get('DATABASE')

def prepare_connect():
    connect = mysql.connector.connect(
        host=HOST,
        user=USER,
        password=PASSWORD,
        database=DATABASE
    )

    cursor = connect.cursor(prepared=True)

    return connect, cursor

# Create
connect, cursor = prepare_connect()
insert_query = 'INSERT INTO products (name, value) VALUES (%s, %s)'
insert_values = ('iphone', 1000)
cursor.execute(insert_query, insert_values)
connect.commit()
cursor.close()
connect.close()

# Read
connect, cursor = prepare_connect()
select_all_query = 'SELECT * FROM products'
cursor.execute(select_all_query)
result = cursor.fetchall()
cursor.close()
connect.close()
print(result)

# Update
# OPT 1
connect, cursor = prepare_connect()
update_query = ('INSERT INTO products (name, value) VALUES (%s, %s)')
update_values = ('iphone', 1710)
cursor.execute(update_query, update_values)
connect.commit()
cursor.close()
connect.close()

#OPT 2 BAD OPT (SQL injection)
# connect, cursor = prepare_connect()
# name = 'iphone'
# valor = 778
# command = f'UPDATE products SET valor = {valor} WHERE name = "{name}"'
# cursor.execute(command)
# connect.commit()
# cursor.close()
# connect.close()

# Delete
connect, cursor = prepare_connect()
delete_query = 'DELETE FROM products WHERE id = %s' 
delete_values = (1, )
cursor.execute(delete_query, delete_values)
connect.commit()
cursor.close()
connect.close()
