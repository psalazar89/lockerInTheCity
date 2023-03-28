'''
Written by Pablo Salazar Navalon 28.03.2023

This file contains the connector to the DB

'''

import pymysql

def mycursor():
      connection = pymysql.connect(host="localhost",
                                   user="root",
                                   password="",
                                   db="lockerDB",
                                   charset="utf8mb4",
                                   cursorclass=pymysql.cursors.DictCursor)

      cursor = connection.cursor()
      return cursor, connection