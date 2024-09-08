import mysql.connector
from mysql.connector import Error
import time

class dp():
    def __init__(self) -> None:
        # Establish a connection to the MySQL database
        connection = mysql.connector.connect(
                host='HOST', #The host name
                database='NAME',  # Database name
                user='USER',  # Database user
                password='PASSWORD'  # Database password
            )
        self.con = connection
        
    def CreateUser(self, name, email, password):
        print(name)
        if self.con.is_connected():
            cursor = self.con.cursor()

            # SQL query to insert a new user
            insert_query = """
                INSERT INTO users (name, email, password, create_time)
                VALUES (%s, %s, %s, %s)
            """

            # Get the current time for the create_time field
            create_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())

            try:
                # Execute the insert query with parameterized inputs
                cursor.execute(insert_query, (name, email, password, create_time))

                # Commit the transaction to save changes
                self.con.commit()

            except mysql.connector.Error as err:
                print(f"Error: {err}")
                # Rollback the transaction in case of error
                self.con.rollback()

            finally:
                cursor.close()

    def CheckUser(self, name):
        if self.con.is_connected():
            try:
                cursor = self.con.cursor()

                # SQL query to fetch the user's password based on the name
                query = "SELECT password FROM users WHERE name = %s"

                # Execute the query using parameterized inputs
                cursor.execute(query, (name,))

                # Fetch the result
                result = cursor.fetchall()
                cursor.close()

                # Return the password if found, otherwise return None
                if result:
                    return result[0]  # Return the password
                else:
                    return None  # Return None if the user is not found 
            except Error as e:
                print("An error happened")
                print(e)