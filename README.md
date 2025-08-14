# BMI_CALCULATOR-PROJECT
BMI Calculator (Advanced) is a Python application built using Tkinter for the graphical user interface and Matplotlib for visualizing BMI ranges. It calculates Body Mass Index based on height and weight, determines the health category (Underweight, Normal, Overweight, Obese), and visually displays the result on a bar chart for better understanding.
# 🐍 Python Project – BMI_CALVULATOR 
## 📂 Project Structure
  ├── main.py # Main Python script
   ├── requirements.txt # Dependencies (if any)
    └── README.md # Project documentation
# Requirements
  Python 3.x
  Any required libraries listed in requirements.txt

# Project Backend Coding

import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt

# Function to calculate BMI
def calculate_bmi():
    try:
        height = float(entry_height.get()) / 100  # Convert cm to meters
        weight = float(entry_weight.get())
        bmi = round(weight / (height ** 2), 2)
        
        # Determine category
        if bmi < 18.5:
            category = "Underweight"
            color = "blue"
        elif 18.5 <= bmi < 24.9:
            category = "Normal weight"
            color = "green"
        elif 25 <= bmi < 29.9:
            category = "Overweight"
            color = "orange"
        else:
            category = "Obese"
            color = "red"
        
        label_result.config(text=f"BMI: {bmi} ({category})", fg=color)
        
        # Plot BMI chart
        plot_bmi_chart(bmi, color)
    
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter valid numeric values.")

# Function to plot BMI chart
def plot_bmi_chart(bmi, color):
    categories = ["Underweight", "Normal", "Overweight", "Obese"]
    ranges = [18.5, 24.9, 29.9, 40]  # Max range for last category
    
    plt.figure(figsize=(6, 3))
    plt.bar(categories, ranges, color=["blue", "green", "orange", "red"], alpha=0.5)
    plt.axhline(y=bmi, color=color, linestyle="--", linewidth=2, label=f"Your BMI: {bmi}")
    plt.legend()
    plt.title("BMI Ranges")
    plt.ylabel("BMI Value")
    plt.show()

# Tkinter UI setup
root = tk.Tk()
root.title("Advanced BMI Calculator")
root.geometry("350x250")
root.configure(bg="#f0f0f0")

tk.Label(root, text="Height (cm):", bg="#f0f0f0", font=("Arial", 12)).pack(pady=5)
entry_height = tk.Entry(root, font=("Arial", 12))
entry_height.pack()

tk.Label(root, text="Weight (kg):", bg="#f0f0f0", font=("Arial", 12)).pack(pady=5)
entry_weight = tk.Entry(root, font=("Arial", 12))
entry_weight.pack()

tk.Button(root, text="Calculate BMI", font=("Arial", 12, "bold"),
          bg="#4CAF50", fg="white", command=calculate_bmi).pack(pady=10)

label_result = tk.Label(root, text="", bg="#f0f0f0", font=("Arial", 14, "bold"))
label_result.pack(pady=10)

root.mainloop()


  
