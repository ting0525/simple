import tkinter as tk
from tkinter import filedialog
import os
import zipfile  

def compress_files(folder_name):
    
    zip_filename = f"{folder_name}.zip"

    
    with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
        
        for i in range(1, len(os.listdir(folder_name)) // 2 + 1):
            in_file = f"{folder_name}/{i}.in"
            zipf.write(in_file, os.path.basename(in_file))

        
        for i in range(1, len(os.listdir(folder_name)) // 2 + 1):
            out_file = f"{folder_name}/{i}.out"
            zipf.write(out_file, os.path.basename(out_file))

    return zip_filename

def process_txt_file():
    
    folder_name = folder_name_entry.get()
    if not folder_name:
        folder_name = "testcase"  

    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if file_path:
        with open(file_path, "r") as file:
            lines = file.readlines()

        input_data = []
        output_data = []
        is_output = False

        for line in lines:
            if line.strip() == "#":
                is_output = True
                continue
            if is_output:
                output_data.append(line.strip())
            else:
                input_data.append(line.strip())

        
        if not os.path.exists(folder_name):
            os.mkdir(folder_name)

        for i in range(len(input_data)):
            with open(f"{folder_name}/{i + 1}.in", "w") as in_file:
                in_file.write(input_data[i])

            with open(f"{folder_name}/{i + 1}.out", "w") as out_file:
                out_file.write(output_data[i])

        
        compressed_filename = compress_files(folder_name)

        result_label.config(text=f"檔案處理完成，已創建'{folder_name}'資料夾，壓縮為'{compressed_filename}'")


root = tk.Tk()
root.title("TXT轉換工具")

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)


folder_name_label = tk.Label(frame, text="請輸入資料夾名稱（預設為'testcase'）:")
folder_name_label.pack()

folder_name_entry = tk.Entry(frame)
folder_name_entry.pack()

process_button = tk.Button(frame, text="選擇並處理TXT檔案", command=process_txt_file)
process_button.pack()

result_label = tk.Label(frame, text="")
result_label.pack()

root.mainloop()
