import tkinter as tk
from datetime import datetime

def calculate_time_difference():
    time_format = "%H:%M"  

    time1 = entry1.get()
    time2 = entry2.get()

    datetime1 = datetime.strptime(time1, time_format)
    datetime2 = datetime.strptime(time2, time_format)

    time_difference = datetime2 - datetime1

    result_label.config(text="time: " + str(time_difference))
    
    clear_text()

def clear_text():
    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)

window = tk.Tk()
window.title("calculate")


entry1 = tk.Entry(window)
entry1.pack()

entry2 = tk.Entry(window)
entry2.pack()


calculate_button = tk.Button(window, text = "計算", command = calculate_time_difference)
calculate_button.pack()


result_label = tk.Label(window, text="time:")
result_label.pack()


window.mainloop()
