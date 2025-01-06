import mysql.connector
from mysql.connector import Error

def connect_to_database():
    connection = None  
    try:
        connection = mysql.connector.connect(
            host="localhost",     
            user="root",          
            password="root@123",  
            database="mysql_node" 
        )

        if connection.is_connected():
            print("Connection to 'mysql_node' database was successful!")
            
            # Retrieve and display database server info
            db_info = connection.get_server_info()
            print(f"MySQL Server version: {db_info}")
            
            # Execute a sample query
            cursor = connection.cursor()
            cursor.execute("SELECT DATABASE();")
            record = cursor.fetchone()
            print(f"Connected to database: {record[0]}")
    
    except Error as e:
        print(f"Error while connecting to MySQL: {e}")
    
    finally:
        # Closing the connection
        if connection and connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed.")

if __name__ == "__main__":
    connect_to_database()




#%%
msg = "Hello World"
print(msg)

#%%
msg = "Hello again"
print(msg)