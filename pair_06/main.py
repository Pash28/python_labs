import tkinter as tk
from tkinter import messagebox
import student_utils

students = ["Anna", "Ivan", "Olha"]


def make_report():
    value = grade_input.get().strip()

    if not value.isdigit() or not 1 <= int(value) <= 20:
        messagebox.showerror("Error", "Enter a number from 1 to 20")
        return

    amount = int(value)
    lines = []

    for name in students:
        marks = student_utils.generate_grades(amount)
        avg = student_utils.average_grade(marks)
        level = student_utils.get_level(avg)
        lines.append(f"{name}: {marks} -> {avg:.1f} -> {level}")

    report = "\n".join(lines)
    print(report)

    result_box.delete("1.0", tk.END)
    result_box.insert(tk.END, report)


app = tk.Tk()
app.title("Student Statistics")
app.geometry("500x400")

tk.Label(app, text="Number of grades (1-20):").pack(pady=5)

grade_input = tk.Entry(app, width=12, justify="center")
grade_input.insert(0, "5")
grade_input.pack(pady=5)

tk.Button(
    app,
    text="Generate report",
    command=make_report,
    bg="seagreen",
    fg="white"
).pack(pady=10)

result_box = tk.Text(app, height=8, width=55)
result_box.pack(padx=10, pady=10)

if __name__ == "__main__":
    app.mainloop()