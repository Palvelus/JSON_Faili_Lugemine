import json
import tkinter as tk
from tkinter import filedialog, messagebox
from person_data import PersonData  # Updated import statement

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Tuntud Eesti Isikud")
        self.create_widgets()

    def create_widgets(self):
        self.load_button = tk.Button(self.root, text="Vali JSON Fail", command=self.load_file)
        self.load_button.pack(pady=20)
        self.results_text = tk.Text(self.root, wrap=tk.WORD, width=80, height=20)
        self.results_text.pack(pady=20)

    def load_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("JSON files", "*.json")])
        if file_path:
            with open(file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)

            self.person_data = PersonData(data)
            self.show_results()
        else:
            messagebox.showwarning("Hoiatus", "Faili ei valitud.")

    def show_results(self):
        results = [
            f"Isikute arv kokku: {self.person_data.total_people()}",
            f"Kõige pikem nimi ja tähemärkide arv: {self.person_data.longest_name()}",
            f"Kõige vanem elav inimene: {self.person_data.oldest_living_person()}",
            f"Kõige vanem surnud inimene: {self.person_data.oldest_deceased_person()}",
            f"Näitlejate koguarv: {self.person_data.total_actors()}",
            f"Sündinud 1997 aastal: {self.person_data.born_in_year(1997)}",
            f"Erinevate elukutsete arv: {self.person_data.unique_occupations()}",
            f"Nimi sisaldab rohkem kui kaks nime: {self.person_data.names_with_more_than_two_parts()}",
            f"Sünniaeg ja surmaaeg on sama v.a. aasta: {self.person_data.birth_death_same_except_year()}",
            f"Elavaid isikuid: {self.person_data.living_and_deceased_count()[0]}, Surnud isikuid: {self.person_data.living_and_deceased_count()[1]}"
        ]

        self.results_text.delete(1.0, tk.END)
        self.results_text.insert(tk.END, "\n".join(results))

# Peamine käivitamine
if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
