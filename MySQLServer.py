#!/usr/bin/python3
"""
This script creates the database alx_book_store in a MySQL server.
"""

import mysql.connector

try:
    # CONNECT TO MYSQL SERVER
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password=""  # Replace with your MySQL password
    )

    cursor = connection.cursor()

    # CREATE DATABASE WITHOUT FAILING IF IT EXISTS
    cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")

    print("Database 'alx_book_store' created successfully!")

except mysql.connector.Error as e:
    print(f"Error while connecting to MySQL: {e}")

finally:
    # CLOSE CURSOR AND CONNECTION
    try:
        cursor.close()
        connection.close()
    except Exception:
        pass
