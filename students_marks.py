import tkinter as tk
from tkinter import messagebox

# Function to calculate the remark based on score
def calculate_remark():
    try:
        # Get input values
        name = name_entry.get().strip()
        course = course_entry.get().strip()
        score = score_entry.get().strip()

        # Debug prints
        print(f"Inputs - Name: {name}, Course: {course}, Score: {score}")

        # Validate inputs
        if not name or not course:
            messagebox.showerror("Input Error", "Please enter all fields.")
            return
        if not score.isdigit():
            messagebox.showerror("Input Error", "Score must be a valid number.")
            return

    
        score = int(score)

        
        if score > 100:
            remark = "Invalid Score"
        elif score >= 70:
            remark = "Distinction"
        elif 50 <= score <= 69:
            remark = "Credit"
        elif 40 <= score <= 49:
            remark = "Pass"
        elif score < 40:
            remark = "Fail"
        else:
            remark = "Invalid Score"

        
        print(f"Remark: {remark}")

        
        result_label.config(
            text=f"Student: {name}\nCourse: {course}\nScore: {score}\nRemark: {remark}",
            fg="green",
        )
    except Exception as e:
        print(f"Error: {e}")
        messagebox.showerror("Input Error", "Unexpected error occurred. Please try again.")

def clear_fields():
    name_entry.delete(0, tk.END)
    course_entry.delete(0, tk.END)
    score_entry.delete(0, tk.END)
    result_label.config(text="")

app = tk.Tk()
app.title("Student Score Remark")
app.geometry("400x500")

tk.Label(app, text="Student Name:", font=("Arial", 12)).pack(pady=5)
name_entry = tk.Entry(app, font=("Arial", 12))
name_entry.pack(pady=5)

tk.Label(app, text="Course:", font=("Arial", 12)).pack(pady=5)
course_entry = tk.Entry(app, font=("Arial", 12))
course_entry.pack(pady=5)

tk.Label(app, text="Score:", font=("Arial", 12)).pack(pady=5)
score_entry = tk.Entry(app, font=("Arial", 12))
score_entry.pack(pady=5)

submit_button = tk.Button(app, text="Submit", command=calculate_remark, font=("Arial", 12), bg="lightblue")
submit_button.pack(pady=10)

clear_button = tk.Button(app, text="Clear", command=clear_fields, font=("Arial", 12), bg="lightcoral")
clear_button.pack(pady=5)

result_label = tk.Label(app, text="", font=("Arial", 12), fg="green")
result_label.pack(pady=10)

app.mainloop()
