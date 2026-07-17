import mysql.connector as ms
import time
import customtkinter as ctk

def dbpassword_requestui():
    #create a new window for the user to enter their database password
    dbpasswindow = ctk.CTk()
    dbpasswindow.title("Database Password")
    dbpasswindow.geometry("400x200")
    dbpasswindow.resizable(False, False)

    ctk.CTkLabel(
        dbpasswindow,
        text="Enter your database password",
        font=("Arial", 18)
    ).place(x=50, y=50)

    dbpassentry = ctk.CTkEntry(
        dbpasswindow,
        width=300,
        placeholder_text="Enter password",
        show="*"
    )
    dbpassentry.place(x=50, y=100)

    def submit_dbpass():
        global dbpass
        dbpass = dbpassentry.get()
        try:
            global db
            db = ms.connect(host="localhost", user="root", password=dbpass)
            print("Connected to the mysql")
            dbpasswindow.destroy()
        except ms.Error as e:
            print("Error connecting to the mysql:", e)
            #kill the program if connection fails
            exit()

    ctk.CTkButton(
        dbpasswindow,
        text="Submit",
        width=300,
        command=submit_dbpass
    ).place(x=50, y=150)

    dbpasswindow.mainloop()
    
def new_userprotocol ():
    #create a new database and table for user credentials
    try:
        cursor = db.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS prism")
        cursor.execute("USE prism")
        cursor.execute("CREATE TABLE IF NOT EXISTS users (id INT AUTO_INCREMENT PRIMARY KEY, username VARCHAR(60), password VARCHAR(60), created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)")
        print("Database and table created successfully.")
    except ms.Error as e:
        print("Error creating database or table:", e)

def insert_user(username, password):
    try:
        cursor = db.cursor()
        cursor.execute("USE prism")
        cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
        db.commit()
        print("User inserted successfully.")
    except ms.Error as e:
        print("Error inserting user:", e)
def user_exists(username, password):
    try:
        cursor = db.cursor()
        cursor.execute("USE prism")
        cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, password))
        result = cursor.fetchone()
        return result is not None
    except ms.Error as e:
        print("Error checking user existence:", e)
        return False


