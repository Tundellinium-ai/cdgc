# from cbt_config import cbtconfig

# class cbtApp(cbtconfig):
#     def __init__(self, School_name, db_name, db_pass):
#         super().__init__(School_name, db_name, db_pass)
#     def home(self):
#         print(f'''The name of the school is {self.get_school_name()}
#         1. Register
#         2. Sign in
#         3. Exit              
#          ''')
#         choice = input("Enter your choice: ")
#         if choice == "1":
#             self.register()
#         elif choice == "2":
#             self.sign_in()
#         elif choice == "3":
#             exit()
#         else:
#             print("Invalid choice")
#     def register(self):
#         fullname = input("Enter Fullname: ")
#         email = input("Enter Email: ")
#         password = input("Enter password: ")
#         result = self.CreateAccount(fullname, email, password)
#         print(result["Message"])
#         if result["status"]:
#             self.sign_in()
#         else:
#             self.home()
#     def sign_in(self):
#         email = input("Enter Email: ").strip()
#         password = input("Enter Password: ").strip()
#         result2 = self.login(email, password)
#         if result2 and result2.get("status"):
#             print(result2["Message"])
#             q = result2["Data"]
#             print(q["fullname"])
#             self.dashboard(q)
#         else:
#             print(result2["error"])

#     def dashboard(self, q):
#         print(f'''
#         Welcome {q["fullname"]}
#         1. Take Test
#         2. Display Result
#         3. Exit
#         ''')
#         choice = input("Enter choice: ")
#         if choice == "1":
#             pass

# app = cbtApp("Sunshine Primary School", "eyedb", "")
# app.home()







# == MYSQL ==
# import mysql.connector as sql

# con = sql.connect(
#     host = "localhost",
#     user = "root",
#     password = ""
# )
# print("database succesfully created.")
# mycursor = con.cursor()
# query = "SHOW DATABASES"
# mycursor.execute(query)
# database = mycursor.fetchall()
# print(database)

# con = sql.connect(
#     host = "localhost",
#     user = "root",
#     password = "",
#     database = "oct_cohort"
# )

# print("database succesfully created.")
# mycursor = con.cursor()
# query = "SHOW TABLES"
# mycursor.execute(query)
# database = mycursor.fetchall()
# print(database)

# con = sql.connect(
#     host = "localhost",
#     user = "root",
#     password = "",
    # database = "oct_cohort"
# )

# print("database succesfully created.")
# mycursor = con.cursor()
# query = "DROP DATABASE oct_cohort"
# query = "CREATE DATABASE oct_cohort"
# mycursor.execute(query)
# database = mycursor.fetchall()
# print(database)

# import mysql.connector as sql

# con = sql.connect(
#     host = "localhost",
#     user = "root",
#     port = "3306",
#     password = "",
#     database = "eyedb"
# )

# print("Database Successfully Connected")

# mycursor = con.cursor()
# query = "SHOW DATABASES"
# mycursor.execute(query)
# database = mycursor.fetchall()
# print(database)

# mycursor = con.cursor()
# query = "DROP DATABASE oct_cohort"
# mycursor.execute(query)

# query = "CREATE DATABASE eyeDB"

# query = '''CREATE TABLE user_table(
# id INT PRIMARY KEY AUTO_INCREMENT,
# fullname VARCHAR(50),
# email VARCHAR(50) UNIQUE,
# account_no VARCHAR(50) UNIQUE,
# account_bal DECIMAL(10,2) DEFAULT 0.0,
# address VARCHAR(50),
# date_created DATETIME DEFAULT CURRENT_TIMESTAMP
#                                     )'''

# query = "ALTER TABLE user_table ADD OR DROP COLUMN matric_no VARCHAR(6);"
# query = "ALTER TABLE user_table CHANGE COLUMN matric_no matric_number VARCHAR(6);"
# query = "RENAME TABLE user_table TO myuser_table"
# mycursor.execute(query)





###############################################
# import mysqlconnector

# connection = mysqlconnector.connect(
#     host = "localhost",
#     user = "root",
#     password = " ",
# )

# cursor = connection.cursor()
# cursor.execute("CREATE A DATABASE IF NOT EXIST ")
# print(" ")
# cursor.close()
# connection.close()

# Error Handling
# runtime errors

# compile-time errors
# e.g. name = "ade"
# print(name
# try
# except
# finally
# else

# File Handling
# r = read
# w = write
# a = append
# x = create
# file = open('file.txt', "x") file = open('file.csv', "x") file = open('file.json', "x")
# file.write("Oh Happy day")
# import json
# import os
# data = {
#     "name": "ade",
#     "age": 23
# }
# with open("Tunde.json", "w") as text:
#     json.dump(data, text)

# os.remove("Tunde.json")

# ===datetime===
# import datetime as dt
# time = dt.datetime.today()
# print(time.strftime("%I:%M%p"))
# format = time.strftime("%Y/%m/%d %I/%M/%S")
# print(f"This the formatted time: {format}")

===regular expression===
import re
password = r"\d+"
pas = input("Enter password: ")
fine = re.match(password, pas)
if fine:
    print("Valid password")

else:
    print(ValueError, )
