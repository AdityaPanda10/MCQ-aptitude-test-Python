import tkinter as tk
from tkinter import messagebox
import mysql.connector

def submit_form():
    name = entry_name.get()
    studentid = entry_id.get()
    rollnumber = entry_roll_number.get()
    
    if name == "" or studentid == "" or rollnumber == "":
        messagebox.showwarning("Input Error", "Please fill out all fields.")
    else:
        db_connection = mysql.connector.connect(
            host="localhost",          
            user="root",               
            password="",  
            database="student_aptitude_test"
        )

        cursor = db_connection.cursor()
        cursor.execute("""
            INSERT INTO students (name, studentid, rollnumber)
            VALUES (%s, %s, %s)
        """, (name, studentid, rollnumber))

        db_connection.commit()

        messagebox.showinfo("Success", f"Student {name} registered successfully!\nID: {studentid}\nRoll No: {rollnumber}")
        
        cursor.close()
        db_connection.close()

root = tk.Tk()
root.title("Student Login Form")
root.geometry("800x600")

heading_label = tk.Label(root, text="Student Registration form for Aptitude Test", font=("Helvetica", 18, "bold"), fg="#2196F3")
heading_label.pack(pady=20)

label_name = tk.Label(root, text="Enter Name:", font=("Helvetica", 15, "bold"))
label_name.pack(pady=15)
entry_name = tk.Entry(root, font=("Helvetica", 12), width=30)
entry_name.pack(pady=10)

label_id = tk.Label(root, text="Enter Student ID:", font=("Helvetica", 15, "bold"))
label_id.pack(pady=15)
entry_id = tk.Entry(root, font=("Helvetica", 12), width=30)
entry_id.pack(pady=10)

label_roll_number = tk.Label(root, text="Enter Roll Number:", font=("Helvetica", 15, "bold"))
label_roll_number.pack(pady=15)
entry_roll_number = tk.Entry(root, font=("Helvetica", 12), width=30)
entry_roll_number.pack(pady=10)

submit_button = tk.Button(root, text="Register", command=submit_form, font=("Helvetica", 12), bg="#2196F3", fg="white", width=20, height=2)
submit_button.pack(pady=20)

root.mainloop()
