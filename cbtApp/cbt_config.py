from random import randint as randy
import mysql.connector as sql
class cbtconfig:
    # __database = []
    __School_name = None
    __host = "localhost"
    __user = "root"
    __port = "3306"
    password = ""
    database = None
    __cursor = None
    __con = None
    
    def __init__(self, School_name, db_name, db_pass):
        self.__School_name = School_name
        self.__database= db_name
        self.__password = db_pass
        try:
            self.__con = sql.connect(
                host = self.__host,
                user = self.__user,
                port = self.__port,
                password = self.__password,
                database = self.__database
            )
            self.__con.autocommit = True
            self.__cursor = self.__con.cursor()
        except sql.Error as a:
            print(f"connection not successful {a}")
    
    def CreateAccount(self, fullname, email,password):
        matric_no = randy(100000, 999999)
        
        # user = {
        #     "fullname" : fullname,
        #     "email" : email,
        #     "matric_no": matric_no,
        #     "password": password
        # }

        # self.__database.append(user)
        try:
            query = "INSERT INTO myuser_table (fullname, email, matric_number, password) VALUES (%s, %s, %s, %s)"
            # query = "ALTER TABLE myuser_table ADD COLUMN password VARCHAR(50)"
            user = (fullname, email, matric_no, password)
            self.__cursor.execute(query, user)
        except sql.IntegrityError as v:
            # print(f"{v}")
            return {
                "status": False,
                "Message": f"{v} Invalid Input"
            }       
        else:
            return {
                "status": True,
                "Message": "Registration Successful!"
            }
    
    def login(self, email, password):
        query2 = "SELECT fullname, email, matric_number FROM myuser_table WHERE email = %s AND password = %s"
        values = (email, password)
        self.__cursor.execute(query2, values)
        user2 = self.__cursor.fetchone()
        if user2:
            return {
                "status": True,
                "Message": "Login Successful!",
                "Data": {
                    "fullname": user2[0],
                    "email": user2[1],
                    "matric": user2[2]
                }
            }
        # for i in self.__database:
        
        #     if i["email"] == email and i["password"] == password:
        #         return{
        #             "status": True,
        #             "Message": "Login Successful!",
        #             "Data": i
        #         }
        else:
            return {
                "status": False,
                "error": "Invalid details"
            }
    def get_school_name(self):
       return self.__School_name
        
