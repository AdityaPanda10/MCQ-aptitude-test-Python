import tkinter as tk

def start_test():
    print("Starting the Aptitude Test...")
    root.destroy()

# Creating the main window (Home Page)
root = tk.Tk()
root.title("Aptitude Test - Home Page")
root.geometry("800x600")  # Set window size
root.configure(bg="#f0f0f0")  # Light gray background color

# Title Label
title_label = tk.Label(root, text="Aptitude Test", font=("Helvetica", 24, "bold"), fg="#2196F3", bg="#f0f0f0")
title_label.pack(pady=30)

# Introduction Text
intro_text = tk.Label(root, text="Welcome to the Aptitude Test!\nTest your skills with multiple choice questions.", font=("Arial", 12), fg="black", bg="#f0f0f0")
intro_text.pack(pady=10)

# Instructions Label
instructions_text = tk.Label(
    root,
    text="Instructions:\n1. You will be given multiple-choice questions.\n2. Select the correct answer from the options.\n3. Click 'Next' to proceed to the next question.\n4. Once done, submit your answers.",
    font=("Times New Roman", 15),
    fg="black",
    bg="#f0f0f0",
    justify="left"
)
instructions_text.pack(pady=10)

# Start Test Button
start_button = tk.Button(root, text="Start Test", font=("Times New Roman", 14, "bold"), bg="#2196F3", fg="black", command=start_test)
start_button.pack(pady=20, ipadx=20, ipady=10)

# Footer Label
footer_label = tk.Label(root, text=" Created by Aditya and Heramb", font=("Courier",20), fg="black", bg="#f0f0f0")
footer_label.pack(side="bottom", pady=10)

root.mainloop()
