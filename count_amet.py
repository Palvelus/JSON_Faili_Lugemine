import json
from collections import Counter
import tkinter as tk
from tkinter import filedialog, ttk

def count_jobs(json_data):
    jobs = [person["amet"] for person in json_data]
    job_counts = Counter(jobs)
    return job_counts

def load_file_and_count_jobs():
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    file_path = filedialog.askopenfilename(filetypes=[("JSON files", "*.json")])
    if not file_path:
        print("No file selected.")
        return

    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    job_counts = count_jobs(data)
    display_results(job_counts)

def display_results(job_counts):
    result_window = tk.Tk()
    result_window.title("Job Counts")

    total_jobs_label = tk.Label(result_window, text=f"Erinevate elukutsete arv: {len(job_counts)}", font=("Helvetica", 16, "bold"))
    total_jobs_label.pack(pady=10)

    frame = ttk.Frame(result_window)
    frame.pack(padx=10, pady=10)

    canvas = tk.Canvas(frame)
    scrollbar = ttk.Scrollbar(frame, orient="vertical", command=canvas.yview)
    scrollable_frame = ttk.Frame(canvas)

    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(
            scrollregion=canvas.bbox("all")
        )
    )

    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

    canvas.configure(yscrollcommand=scrollbar.set)

    for job, count in job_counts.items():
        job_label = ttk.Label(scrollable_frame, text=f"{job}: {count}")
        job_label.pack(anchor="w", padx=5, pady=2)

    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    result_window.mainloop()

if __name__ == "__main__":
    load_file_and_count_jobs()
