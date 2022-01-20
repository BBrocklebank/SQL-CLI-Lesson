import os
import pymysql


# Get username from gitpod wokrspace
# (modify this variable if running on another environment)
username = os.getenv('C9_USER')

# Connect to the database
connection = pymysql.connect(host='localhost',
                                    user=username,
                                    password='',
                                    db='Chinook')

try:
    # Run a query
    with connection.cursor() as cursor:
        sql = "select * from Artist;"
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)
finally:
    # Close the connection, regardless of whethere it was a success or not
    connection.close()