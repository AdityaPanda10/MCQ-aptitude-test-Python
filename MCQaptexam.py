import tkinter as tk
from tkinter import messagebox
import mysql.connector

# Global variables
student_info = {"name": "", "studentid": "", "rollnumber": ""}
questions = [
    {
        "question": "What is the output of: print(2 ** 3)?",
        "options": ["6", "8", "9", "5"],
        "answer": "8"
    },
    {
        "question": "Which keyword is used to define a function in Python?",
        "options": ["function", "def", "define", "func"],
        "answer": "def"
    },
    {
        "question": "What data type is the object: x = [1, 2, 3]?",
        "options": ["Tuple", "List", "Dictionary", "Set"],
        "answer": "List"
    },
    {
        "question": "Which keyword is used for a loop in Python?",
        "options": ["loop", "iterate", "for", "repeat"],
        "answer": "for"
    },
    {
        "question": "What will `print(type('10'))` return?",
        "options": ["int", "str", "float", "bool"],
        "answer": "str"
    },
    {
        "question": "Which operator is used for floor division in Python?",
        "options": ["/", "//", "%", "**"],
        "answer": "//"
    },
    {
        "question": "What does `len()` function do?",
        "options": ["Counts characters", "Finds maximum", "Finds minimum", "Returns the last item"],
        "answer": "Counts characters"
    },
    {
        "question": "What is the correct way to write a comment in Python?",
        "options": ["// this is a comment", "/* comment */", "# this is a comment", "-- comment"],
        "answer": "# this is a comment"
    },
    {
        "question": "Which method is used to add an item to a list?",
        "options": ["insert()", "add()", "append()", "extend()"],
        "answer": "append()"
    },
    {
        "question": "What will be the output of `bool(0)`?",
        "options": ["True", "False", "0", "None"],
        "answer": "False"
    },
    {
        "question": "What is the output of `3 == 3.0`?",
        "options": ["True", "False", "Error", "None"],
        "answer": "True"
    },
    {
        "question": "What is the output of: `print('Hello' * 2)`?",
        "options": ["Hello2", "Hello Hello", "HelloHello", "Error"],
        "answer": "HelloHello"
    },
    {
        "question": "What is used to handle exceptions in Python?",
        "options": ["try-catch", "try-except", "error-handling", "if-else"],
        "answer": "try-except"
    },
    {
        "question": "What is a correct syntax to import a module?",
        "options": ["include math", "using math", "import math", "require math"],
        "answer": "import math"
    },
    {
        "question": "What keyword is used to create a class?",
        "options": ["object", "def", "class", "module"],
        "answer": "class"
    },
    {
        "question": "Which of the following is a mutable data type?",
        "options": ["Tuple", "List", "String", "Integer"],
        "answer": "List"
    },
    {
        "question": "What is the output of `10 % 3`?",
        "options": ["1", "0", "3", "10"],
        "answer": "1"
    },
    {
        "question": "Which function is used to get input from the user?",
        "options": ["scan()", "get()", "read()", "input()"],
        "answer": "input()"
    },
    {
        "question": "Which of these is not a core data type in Python?",
        "options": ["List", "Dictionary", "Class", "Tuple"],
        "answer": "Class"
    },
    {
        "question": "What is the output of `type([])`?",
        "options": ["list", "<class 'list'>", "ListType", "array"],
        "answer": "<class 'list'>"
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

        student_info.update({"name": name, "studentid": studentid, "rollnumber": rollnumber})

        messagebox.showinfo("Success", f"Registered Successfully!")
        registration_window.destroy()
        show_home_page()

    except Exception as e:
        messagebox.showerror("Database Error", str(e))

def show_home_page():
    home_page = tk.Tk()
    home_page.title("Aptitude Test - Home Page")
    home_page.geometry("1024x600")
    home_page.configure(bg="#e8f5e9")

    tk.Label(home_page, text="Welcome to the Aptitude Test!", font=("Georgia", 28, "bold"), fg="#1b5e20", bg="#e8f5e9").pack(pady=30)
    tk.Label(home_page, text="Test your skills with multiple choice questions.", font=("Georgia", 16), fg="#1b5e20", bg="#e8f5e9").pack()

    tk.Label(home_page, text="Instructions:\n1. Answer each MCQ.\n2. Click Next to proceed.\n3. Score will be shown at the end.", font=("Georgia", 16), fg="#1b5e20", bg="#e8f5e9", justify="left").pack(pady=20)

    tk.Button(home_page, text="Start Test", font=("Georgia", 16, "bold"), bg="#388e3c", fg="white", command=lambda: start_test(home_page)).pack(pady=30)

    tk.Label(home_page, text="Created by Aditya and Heramb", font=("Georgia", 14), fg="#1b5e20", bg="#e8f5e9").pack(side="bottom", pady=10)
    home_page.mainloop()

def start_test(home_page):
    home_page.destroy()
    init_test_window()

def init_test_window():
    global question_window, question_label, option_buttons, var
    question_window = tk.Tk()
    question_window.title("MCQ Test")
    question_window.geometry("1024x600")
    question_window.configure(bg="#e8f5e9")

    var = tk.StringVar()

    question_label = tk.Label(question_window, font=("Georgia", 20, "bold"), wraplength=900, justify="left", fg="#1b5e20", bg="#e8f5e9")
    question_label.pack(pady=30)

    option_buttons = []
    for _ in range(4):
        btn = tk.Radiobutton(question_window, variable=var, font=("Georgia", 16), wraplength=800, justify="left", anchor="w", fg="#1b5e20", bg="#e8f5e9", selectcolor="#c8e6c9")
        btn.pack(anchor="w", padx=50, pady=5)
        option_buttons.append(btn)

    next_btn = tk.Button(question_window, text="Next", font=("Georgia", 16, "bold"), bg="#388e3c", fg="white", command=next_question)
    next_btn.pack(pady=30)

    display_question()
    question_window.mainloop()

def display_question():
    question = questions[current_question_index]
    question_label.config(text=f"Q{current_question_index + 1}: {question['question']}")
    var.set(None)
    for i, opt in enumerate(question["options"]):
        option_buttons[i].config(text=opt, value=opt)

def next_question():
    global current_question_index, score
    selected = var.get()
    if selected == questions[current_question_index]["answer"]:
        score += 1

    current_question_index += 1
    if current_question_index < len(questions):
        display_question()
    else:
        question_window.destroy()
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
        """, (student_info["name"], student_info["studentid"], student_info["rollnumber"], score))
        db_connection.commit()
        cursor.close()
        db_connection.close()
    except Exception as e:
        messagebox.showerror("Database Error", str(e))

def show_result():
    submit_score_to_db()

    result_window = tk.Tk()
    result_window.title("Test Result")
    result_window.geometry("1024x600")
    result_window.configure(bg="#e8f5e9")

    tk.Label(result_window, text=f"Test Completed!", font=("Georgia", 28, "bold"), fg="#1b5e20", bg="#e8f5e9").pack(pady=50)
    tk.Label(result_window, text=f"Your Score: {score}/{len(questions)}", font=("Georgia", 22), fg="#1b5e20", bg="#e8f5e9").pack(pady=30)

    tk.Button(result_window, text="Close", command=result_window.destroy, bg="#388e3c", fg="white", font=("Georgia", 16, "bold"), width=15).pack(pady=30)

    result_window.mainloop()

# Registration window
registration_window = tk.Tk()
registration_window.title("Student Registration")
registration_window.geometry("1024x600")
registration_window.configure(bg="#e8f5e9")

label_style = {"font": ("Georgia", 16), "fg": "#1b5e20", "bg": "#e8f5e9"}

tk.Label(registration_window, text="Student Registration Form", font=("Georgia", 24, "bold"), fg="#1b5e20", bg="#e8f5e9").pack(pady=20)

tk.Label(registration_window, text="Name:", **label_style).pack(pady=10)
entry_name = tk.Entry(registration_window, font=("Georgia", 14), width=40)
entry_name.pack()

tk.Label(registration_window, text="Student ID:", **label_style).pack(pady=10)
entry_id = tk.Entry(registration_window, font=("Georgia", 14), width=40)
entry_id.pack()

tk.Label(registration_window, text="Roll Number:", **label_style).pack(pady=10)
entry_roll_number = tk.Entry(registration_window, font=("Georgia", 14), width=40)
entry_roll_number.pack()

tk.Button(registration_window, text="Register", command=submit_form, font=("Georgia", 16, "bold"), bg="#388e3c", fg="white", width=20).pack(pady=30)

registration_window.mainloop()