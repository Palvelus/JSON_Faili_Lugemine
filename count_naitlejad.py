import csv
import tkinter as tk
from tkinter import filedialog

def count_naitlejad(csv_file_path):
    count = 0
    with open(csv_file_path, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['amet'] == 'näitleja':
                count += 1
    return count

def browse_file():
    filename = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    if filename:
        count = count_naitlejad(filename)
        result_label.config(text=f"Total number of 'näitleja': {count}")
    else:
        result_label.config(text="No file selected.")

# Create the main window
root = tk.Tk()
root.title("Count Näitlejad")

# Create the Browse button
browse_button = tk.Button(root, text="Browse", command=browse_file)
browse_button.pack(pady=20)

# Create the label to display the result
result_label = tk.Label(root, text="")
result_label.pack()

# Run the GUI
root.mainloop()
