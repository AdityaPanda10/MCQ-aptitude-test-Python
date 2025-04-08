import tkinter as tk
from tkinter import messagebox
import mysql.connector

# Global variables to store student info
student_info = {
    "name": "",
    "studentid": "",
    "rollnumber": ""
}

# Sample MCQs
questions = [
    {
        "question": "Who am I, according to Advaita Vedanta?",
        "options": ["The body", "The mind", "The ego", "The Self (Atman)"],
        "answer": "The Self (Atman)"
    },
    {
        "question": "Which Upanishadic phrase means 'That Thou Art'?",
        "options": ["Tat Tvam Asi", "Aham Brahmasmi", "Neti Neti", "Sarvam Khalvidam Brahma"],
        "answer": "Tat Tvam Asi"
    }
]

current_question_index = 0
score = 0

def submit_form():
    global student_info
    name = entry_name.get().strip()
    studentid = entry_id.get().strip()
    rollnumber = entry_roll_number.get().strip()

    if name == "" or studentid == "" or rollnumber == "":
        messagebox.showwarning("Input Error", "Please fill out all fields.")
        return

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
        cursor.close()
        db_connection.close()

        student_info["name"] = name
        student_info["studentid"] = studentid
        student_info["rollnumber"] = rollnumber

        messagebox.showinfo("Success", f"Student {name} registered successfully!\nID: {studentid}\nRoll No: {rollnumber}")
        registration_window.destroy()
        show_home_page()

    except Exception as e:
        messagebox.showerror("Database Error", f"An error occurred while connecting to the database:\n{str(e)}")

def show_home_page():
    home_page = tk.Tk()
    home_page.title("Aptitude Test - Home Page")
    home_page.geometry("800x600")
    home_page.configure(bg="#f0f0f0")

    tk.Label(home_page, text="Aptitude Test", font=("Helvetica", 24, "bold"), fg="#2196F3", bg="#f0f0f0").pack(pady=30)
    tk.Label(home_page, text="Welcome to the Aptitude Test!\nTest your skills with multiple choice questions.", font=("Arial", 12), bg="#f0f0f0").pack(pady=10)

    tk.Label(home_page, text="Instructions:\n1. You will be given multiple-choice questions.\n2. Select the correct answer.\n3. Click 'Next' to move forward.\n4. Submit your test at the end.", font=("Times New Roman", 15), bg="#f0f0f0", justify="left").pack(pady=10)

    tk.Button(home_page, text="Start Test", font=("Times New Roman", 14, "bold"), bg="#2196F3", fg="black", command=lambda: start_test(home_page)).pack(pady=20, ipadx=20, ipady=10)

    tk.Label(home_page, text="Created by Aditya and Heramb", font=("Courier", 20), bg="#f0f0f0").pack(side="bottom", pady=10)
    home_page.mainloop()

def start_test(home_page):
    home_page.destroy()
    show_question()

def show_question():
    global question_window, var

    question = questions[current_question_index]

    question_window = tk.Tk()
    question_window.title("MCQ Test")
    question_window.geometry("800x600")

    tk.Label(question_window, text=question["question"], font=("Helvetica", 16, "bold")).pack(pady=20)

    var = tk.StringVar()
    for option in question["options"]:
        tk.Radiobutton(question_window, text=option, variable=var, value=option, font=("Helvetica", 14)).pack(anchor="w")

    tk.Button(question_window, text="Next", command=next_question, bg="#4CAF50", fg="white", font=("Helvetica", 20)).pack(pady=20)

    question_window.mainloop()

def next_question():
    global current_question_index, score, var, question_window

    selected_answer = var.get()
    if selected_answer == questions[current_question_index]["answer"]:
        score += 1

    current_question_index += 1
    question_window.destroy()

    if current_question_index < len(questions):
        show_question()
    else:
        show_result()

def submit_score_to_db():
    try:
        db_connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="student_aptitude_test"
        )
        cursor = db_connection.cursor()
        cursor.execute("""
            INSERT INTO scores (name, studentid, rollnumber, score)
            VALUES (%s, %s, %s, %s)
        """, (
            student_info["name"],
            student_info["studentid"],
            student_info["rollnumber"],
            score
        ))
        db_connection.commit()
        cursor.close()
        db_connection.close()
    except Exception as e:
        messagebox.showerror("Database Error", f"Could not save score: {str(e)}")

def show_result():
    result_window = tk.Tk()
    result_window.title("Test Result")
    result_window.geometry("400x400")

    tk.Label(result_window, text=f"Test Completed!\nYour Score: {score}/{len(questions)}", font=("Helvetica", 25, "bold")).pack(pady=40)
    submit_score_to_db()

    tk.Button(result_window, text="Close", command=result_window.destroy, bg="red", fg="white", font=("Helvetica", 15)).pack()
    result_window.mainloop()

# Registration Form
registration_window = tk.Tk()
registration_window.title("Student Registration Form")
registration_window.geometry("800x600")

tk.Label(registration_window, text="Student Registration form for Aptitude Test", font=("Helvetica", 18, "bold"), fg="#2196F3").pack(pady=20)

tk.Label(registration_window, text="Enter Your Name:", font=("Helvetica", 15, "bold")).pack(pady=15)
entry_name = tk.Entry(registration_window, font=("Helvetica", 12), width=30)
entry_name.pack(pady=10)

tk.Label(registration_window, text="Enter Your Student ID:", font=("Helvetica", 15, "bold")).pack(pady=15)
entry_id = tk.Entry(registration_window, font=("Helvetica", 12), width=30)
entry_id.pack(pady=10)

tk.Label(registration_window, text="Enter your Roll Number:", font=("Helvetica", 15, "bold")).pack(pady=15)
entry_roll_number = tk.Entry(registration_window, font=("Helvetica", 12), width=30)
entry_roll_number.pack(pady=10)

tk.Button(registration_window, text="Register", command=submit_form, font=("Helvetica", 12), bg="#2196F3", fg="white", width=20, height=2).pack(pady=20)

registration_window.mainloop()
