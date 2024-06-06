import json
import tkinter as tk
from tkinter import filedialog
from person_data import PersonData


class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Person Data Viewer")

        self.load_button = tk.Button(root, text="Load JSON File", command=self.load_file)
        self.load_button.pack(pady=20)

        self.result_text = tk.Text(root, wrap=tk.WORD, width=80, height=20)
        self.result_text.pack(pady=20)

    def load_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("JSON files", "*.json")])
        if not file_path:
            return

        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)

        self.person_data = PersonData(data)
        self.show_results()

    def show_results(self):
        self.result_text.delete(1.0, tk.END)

        results_data = self.person_data.get_results()

        results = [
            "Isikute arv kokku: {}".format(results_data["total_count"]),
            "Kõige pikem nimi ja tähemärkide arv: {} ({} tähemärki)".format(
                results_data["longest_name"].name,
                len(results_data["longest_name"].name)
            ),
            "Kõige vanem elav inimene: {}, {} ({})".format(
                results_data["oldest_living_person"].name,
                results_data["oldest_living_person"].age(),
                results_data["oldest_living_person"].birth_date_estonian()
            ),
            "Kõige vanem surnud inimene: {}, {} ({} - {})".format(
                results_data["oldest_deceased_person"].name,
                results_data["oldest_deceased_person"].age(),
                results_data["oldest_deceased_person"].birth_date_estonian(),
                results_data["oldest_deceased_person"].death_date_estonian()
            ),
            "Näitlejate koguarv: {}".format(results_data["actor_count"]),
            "Sündinud 1997 aastal: {}".format(results_data["count_born_in_1997"]),
            "Erinevate elukutsete arv: {}".format(results_data["unique_occupations"]),
            "Nimi sisaldab rohkem kui kaks nime: {}".format(results_data["multi_name_count"]),
            "Sünniaeg ja surmaaeg on sama v.a. aasta: {}".format(results_data["same_birth_death_month_day"]),
            "Elavaid isikuid: {}, Surnud isikuid: {}".format(
                results_data["living_count"], results_data["deceased_count"]
            )
        ]

        for result in results:
            self.result_text.insert(tk.END, result + "\n")


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
