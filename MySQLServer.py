#!/usr/bin/python3
"""
This script creates the database alx_book_store in a MySQL server.
"""

import mysql.connector
from mysql.connector import Error

try:
    # CONNECT TO MYSQL SERVER
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password=""  
    )

    if connection.is_connected():
        cursor = connection.cursor()

        # CREATE DATABASE 
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")

        print("Database 'alx_book_store' created successfully!")

except Error as e:
    print(f"Error while connecting to MySQL: {e}")

finally:
    # CLOSE CURSOR AND CONNECTION
    if 'cursor' in locals():
        cursor.close()
    if 'connection' in locals() and connection.is_connected():
        connection.close()
