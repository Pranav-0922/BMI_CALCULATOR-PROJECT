import tkinter as tk
from tkinter import messagebox
import csv
import os
import matplotlib.pyplot as plt

# CSV file to store BMI history
HISTORY_FILE = "bmi_history.csv"

# Ensure history file exists
if not os.path.exists(HISTORY_FILE):
    with open(HISTORY_FILE, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Weight (kg)", "Height (m)", "BMI", "Category"])


def calculate_bmi(weight, height):
    """Calculate BMI."""
    return weight / (height ** 2)


def categorize_bmi(bmi):
    """Categorize BMI."""
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"


def save_to_history(weight, height, bmi, category):
    """Save BMI record to CSV file."""
    with open(HISTORY_FILE, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([weight, height, round(bmi, 2), category])


def show_history_graph():
    """Display BMI history as a color-coded bar chart."""
    weights = []
    bmis = []
    categories = []

    with open(HISTORY_FILE, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            weights.append(float(row["Weight (kg)"]))
            bmis.append(float(row["BMI"]))
            categories.append(row["Category"])

    if not bmis:
        messagebox.showinfo("No Data", "No BMI history to display yet.")
        return

    # Assign colors based on category
    colors = []
    for cat in categories:
        if cat == "Underweight":
            colors.append("skyblue")
        elif cat == "Normal weight":
            colors.append("green")
        elif cat == "Overweight":
            colors.append("orange")
        else:
            colors.append("red")

    # Create plot
    plt.figure(figsize=(8, 5))
    bars = plt.bar(range(len(bmis)), bmis, tick_label=weights, color=colors)

    # Add horizontal lines for BMI thresholds
    for threshold in [18.5, 25, 30]:
        plt.axhline(y=threshold, color="gray", linestyle="--", linewidth=1)

    # Add labels on bars
    for bar, bmi in zip(bars, bmis):
        plt.text(bar.get_x() + bar.get_width() / 2,
                 bar.get_height() + 0.1,
                 f"{bmi:.1f}",
                 ha="center", fontsize=9, fontweight="bold")

    plt.xlabel("Weight (kg)")
    plt.ylabel("BMI")
    plt.title("BMI History (Color-Coded by Category)")
    plt.tight_layout()
    plt.show()


def on_calculate():
    """Calculate and display BMI in GUI."""
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get())

        if not (10 <= weight <= 300):
            raise ValueError("Weight must be between 10kg and 300kg.")
        if not (0.5 <= height <= 2.5):
            raise ValueError("Height must be between 0.5m and 2.5m.")

        bmi = calculate_bmi(weight, height)
        category = categorize_bmi(bmi)

        result_label.config(text=f"BMI: {bmi:.2f} ({category})")
        save_to_history(weight, height, bmi, category)

    except ValueError as e:
        messagebox.showerror("Input Error", str(e))


# ----------------- GUI Setup -----------------
root = tk.Tk()
root.title("BMI Calculator (Advanced)")
root.geometry("350x250")
root.resizable(False, False)

# Weight input
tk.Label(root, text="Weight (kg):").pack(pady=5)
weight_entry = tk.Entry(root)
weight_entry.pack()

# Height input
tk.Label(root, text="Height (m):").pack(pady=5)
height_entry = tk.Entry(root)
height_entry.pack()

# Calculate button
tk.Button(root, text="Calculate BMI", command=on_calculate).pack(pady=10)

# Result label
result_label = tk.Label(root, text="", font=("Arial", 12, "bold"))
result_label.pack(pady=5)

# Show history button
tk.Button(root, text="Show BMI History Graph", command=show_history_graph).pack(pady=10)

root.mainloop()
