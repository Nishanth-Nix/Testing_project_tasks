import mysql.connector
from mysql.connector import Error

def main():
    try:
        #1.connect to the data base
        con=mysql.connector.connect(
            host='localhost',
            user="root",
            password="vimalraj2711",
            database='d'
        )

        if con.is_connected():
            print("Connected Successfully Now Start Your code!!!")
        else:
            print("Not yet Connected")
        #insert
        cursor=con.cursor()


        name=input("Enter the name :")
        password=input("Enter the password :")
        sql_insert = "INSERT INTO students (name, password) VALUES (%s, %s)"
        cursor.execute(sql_insert, (name, password))
        con.commit()
        print("Insertion Completed Sucessfully")
       

        #update
        pass1=input("Enter the new password: ")
        name1=input("Enter the updated Nmae:")
        sql_update = "UPDATE students SET password=%s WHERE name=%s"
        cursor.execute(sql_update, (pass1, name1))
        con.commit()
        print("Updated successfully")

        #Display
        sql_view = "SELECT * FROM students"
        cursor.execute(sql_view)
        rows = cursor.fetchall()
        for row in rows:
            print(f"Name: {row[0]} : Password: {row[1]}")
        print("----------------Display Completed------------------")

        # Delete
        name2 = input("Enter the name to delete: ")
        sql_delete = "DELETE FROM students WHERE name=%s"
        cursor.execute(sql_delete, (name2,))
        con.commit()
        print(f"Deleted user {name2} successfully.")

    except mysql.connector.Error as err:
        print("Error:", err)
if __name__ == "__main__":
    main()

