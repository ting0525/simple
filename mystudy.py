import tkinter as tk
from datetime import datetime

def calculate_time_difference():
    time_format = "%H:%M:%S"  # 時間格式

    # 獲取用戶輸入的時間
    time1 = entry1.get()
    time2 = entry2.get()

    # 將時間字符串轉換為datetime對象
    datetime1 = datetime.strptime(time1, time_format)
    datetime2 = datetime.strptime(time2, time_format)

    # 計算時間差
    time_difference = datetime2 - datetime1

    # 在結果標籤中顯示時間差
    result_label.config(text="時間差: " + str(time_difference))

# 創建主視窗
window = tk.Tk()
window.title("時間差計算器")

# 創建時間輸入框
entry1 = tk.Entry(window)
entry1.pack()

entry2 = tk.Entry(window)
entry2.pack()

# 創建計算按鈕
calculate_button = tk.Button(window, text="計算時間差", command=calculate_time_difference)
calculate_button.pack()

# 創建結果標籤
result_label = tk.Label(window, text="時間差:")
result_label.pack()

# 啟動主迴圈
window.mainloop()
