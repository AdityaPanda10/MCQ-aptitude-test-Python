import tkinter as tk
from tkinter import messagebox
import mysql.connector

def start_test():
    print("Starting the Aptitude Test...")
    root.destroy()

def submit_form():
    name = entry_name.get()
    studentid = entry_id.get()
    rollnumber = entry_roll_number.get()
    
    if name == "" or studentid == "" or rollnumber == "":
        messagebox.showwarning("Input Error", "Please fill out all fields.")
    else:
        try:
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

            # Close the registration window and go to the Aptitude Test Home Page
            registration_window.destroy()
            show_home_page()

        except Exception as e:
            messagebox.showerror("Database Error", f"An error occurred while connecting to the database: {str(e)}")


def show_home_page():
    # Creating the main window (Home Page)
    home_page = tk.Tk()
    home_page.title("Aptitude Test - Home Page")
    home_page.geometry("800x600")  # Set window size
    home_page.configure(bg="#f0f0f0")  # Light gray background color

    # Title Label
    title_label = tk.Label(home_page, text="Aptitude Test", font=("Helvetica", 24, "bold"), fg="#2196F3", bg="#f0f0f0")
    title_label.pack(pady=30)

    # Introduction Text
    intro_text = tk.Label(home_page, text="Welcome to the Aptitude Test!\nTest your skills with multiple choice questions.", font=("Arial", 12), fg="black", bg="#f0f0f0")
    intro_text.pack(pady=10)

    # Instructions Label
    instructions_text = tk.Label(
        home_page,
        text="Instructions:\n1. You will be given multiple-choice questions.\n2. Select the correct answer from the options.\n3. Click 'Next' to proceed to the next question.\n4. Once done, submit your answers.",
        font=("Times New Roman", 15),
        fg="black",
        bg="#f0f0f0",
        justify="left"
    )
    instructions_text.pack(pady=10)

    # Start Test Button
    start_button = tk.Button(home_page, text="Start Test", font=("Times New Roman", 14, "bold"), bg="#2196F3", fg="black", command=start_test)
    start_button.pack(pady=20, ipadx=20, ipady=10)

    # Footer Label
    footer_label = tk.Label(home_page, text=" Created by Aditya and Heramb", font=("Courier", 20), fg="black", bg="#f0f0f0")
    footer_label.pack(side="bottom", pady=10)

    home_page.mainloop()

# Creating the Registration Form (Window)
registration_window = tk.Tk()
registration_window.title("Student Registration Form")
registration_window.geometry("800x600")

heading_label = tk.Label(registration_window, text="Student Registration form for Aptitude Test", font=("Helvetica", 18, "bold"), fg="#2196F3")
heading_label.pack(pady=20)

label_name = tk.Label(registration_window, text="Enter Your Name:", font=("Helvetica", 15, "bold"))
label_name.pack(pady=15)
entry_name = tk.Entry(registration_window, font=("Helvetica", 12), width=30)
entry_name.pack(pady=10)

label_id = tk.Label(registration_window, text="Enter Your Student ID:", font=("Helvetica", 15, "bold"))
label_id.pack(pady=15)
entry_id = tk.Entry(registration_window, font=("Helvetica", 12), width=30)
entry_id.pack(pady=10)

label_roll_number = tk.Label(registration_window, text="Enter your Roll Number:", font=("Helvetica", 15, "bold"))
label_roll_number.pack(pady=15)
entry_roll_number = tk.Entry(registration_window, font=("Helvetica", 12), width=30)
entry_roll_number.pack(pady=10)

submit_button = tk.Button(registration_window, text="Register", command=submit_form, font=("Helvetica", 12), bg="#2196F3", fg="white", width=20, height=2)
submit_button.pack(pady=20)

registration_window.mainloop()
