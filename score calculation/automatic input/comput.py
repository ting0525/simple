import tkinter as tk
from tkinter import messagebox
import csv
import matplotlib.pyplot as plt

class GradeCalculatorApp:
    def __init__(self):
        self.n = 0
        self.label_scores = []
        self.entry_scores = []
        self.label_credits = []
        self.entry_credits = []

        self.window = tk.Tk()
        self.window.title("成績計算器")

        self.button_select_file = tk.Button(self.window, text="選擇檔案", command=self.open_file_dialog)
        self.button_select_file.grid(row=0, column=2, padx=10, pady=5)

        self.button_calculate = tk.Button(self.window, text="計算", command=self.calculate_weighted_average)
        self.result_label = tk.Label(self.window, text="", font=("Arial", 14))
        self.window.protocol("WM_DELETE_WINDOW", self.close_window)


    def calculate_weighted_average(self):
        scores = [float(entry_score.get()) for entry_score in self.entry_scores]
        credits = [float(entry_credit.get()) for entry_credit in self.entry_credits]

        if len(scores) != self.n or len(credits) != self.n:
            messagebox.showerror("Error", "The number of scores and credits should be the same as n.")
            return

        weighted_sum = sum(score * credit for score, credit in zip(scores, credits))
        total_credits = sum(credits)
        average = weighted_sum / total_credits

        self.result_label.config(text=f"The weighted average is: {average:.2f}")

        # 繪製折線圖
        plt.plot(range(1, self.n+1), scores, marker='o')
        plt.xlabel('Subject')
        plt.ylabel('Score')
        plt.title('Scores')
        plt.show()

    def read_csv(self, filename):
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                data = list(reader)
                self.n = len(data)

                for widget in self.window.winfo_children():
                    widget.grid_forget()

                for i in range(self.n):
                    self.label_scores.append(tk.Label(self.window, text=f"科目 {i+1} 成績:"))
                    self.label_scores[i].grid(row=i+1, column=0, padx=10, pady=5)

                    self.entry_scores.append(tk.Entry(self.window))
                    self.entry_scores[i].grid(row=i+1, column=1, padx=10, pady=5)
                    self.entry_scores[i].insert(tk.END, data[i]['成績'])

                    self.label_credits.append(tk.Label(self.window, text=f"科目 {i+1} 學分數:"))
                    self.label_credits[i].grid(row=i+1, column=2, padx=10, pady=5)

                    self.entry_credits.append(tk.Entry(self.window))
                    self.entry_credits[i].grid(row=i+1, column=3, padx=10, pady=5)
                    self.entry_credits[i].insert(tk.END, data[i]['學分'])

                self.button_calculate.grid(row=self.n+1, column=0, columnspan=4, padx=10, pady=10)
                self.result_label.grid(row=self.n+2, column=0, columnspan=4, padx=10, pady=5)

        except FileNotFoundError:
            messagebox.showerror("Error", "The file does notexist.")

    def open_file_dialog(self):
        from tkinter import filedialog
        filename = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
        if filename:
            self.read_csv(filename)

    def run(self):
        self.window.mainloop()
    
    def close_window(self):
        self.window.destroy()

if __name__ == "__main__":
    app = GradeCalculatorApp()
    app.run()
    app.close_window()
