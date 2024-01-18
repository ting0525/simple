import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt

def calculate_weighted_average():
    n = int(entry_n.get())

    scores = [float(entry_score.get()) for entry_score in entry_scores]
    credits = [float(entry_credit.get()) for entry_credit in entry_credits]

    if len(scores) != n or len(credits) != n:
        messagebox.showerror("Error", "The number of scores and credits should be the same as n.")
        return

    weighted_sum = sum(score * credit for score, credit in zip(scores, credits))
    total_credits = sum(credits)
    average = weighted_sum / total_credits

    result_label.config(text=f"The weighted average is: {average:.2f}")

    # 繪製折線圖
    plt.plot(range(1, n+1), scores, marker='o')
    plt.xlabel('Subject')
    plt.ylabel('Score')
    plt.title('Scores')
    plt.show()

# 創建主視窗
window = tk.Tk()
window.title("成績計算器")

# 創建輸入框
label_n = tk.Label(window, text="輸入科目數量n:")
label_n.grid(row=0, column=0, padx=10, pady=5)

entry_n = tk.Entry(window)
entry_n.grid(row=0, column=1, padx=10, pady=5)

label_scores = []
entry_scores = []
label_credits = []
entry_credits = []

def create_input_fields():
    n = int(entry_n.get())
    for widget in window.winfo_children():
        widget.grid_forget()

    label_n.grid(row=0, column=0, padx=10, pady=5)
    entry_n.grid(row=0, column=1, padx=10, pady=5)

    for i in range(n):
        label_scores.append(tk.Label(window, text=f"科目 {i+1} 成績:"))
        label_scores[i].grid(row=i+1, column=0, padx=10, pady=5)

        entry_scores.append(tk.Entry(window))
        entry_scores[i].grid(row=i+1, column=1, padx=10, pady=5)

        label_credits.append(tk.Label(window, text=f"科目 {i+1} 學分數:"))
        label_credits[i].grid(row=i+1, column=2, padx=10, pady=5)

        entry_credits.append(tk.Entry(window))
        entry_credits[i].grid(row=i+1, column=3, padx=10, pady=5)

    button_calculate.grid(row=n+1, column=0, columnspan=4, padx=10, pady=10)
    result_label.grid(row=n+2, column=0, columnspan=4, padx=10, pady=5)

# 創建輸入科目數量的按鈕
button_n = tk.Button(window, text="確定", command=create_input_fields)
button_n.grid(row=0, column=2, padx=10, pady=5)

# 創建計算按鈕
button_calculate = tk.Button(window, text="計算", command=calculate_weighted_average)

# 創建顯示結果的Label
result_label = tk.Label(window, text="", font=("Arial", 14))

# 啟動主視窗的事件迴圈
window.mainloop()