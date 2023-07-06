import csv
from bs4 import BeautifulSoup
from tkinter import Tk, filedialog
from comput import GradeCalculatorApp

# 解析HTML並找到目標表格
def parse_html(html):
    soup = BeautifulSoup(html, 'html.parser')
    tables = soup.find_all('table')
    return tables[-1]  # 假設我們只需要提取最後一個表格中的數據

# 解析表格並提取資料
def extract_data(table):
    data = []
    rows = table.find_all('tr')
    for row in rows:
        cells = row.find_all('td')
        if len(cells) >= 6:  # 確保列數正確，以排除表格的表頭和其他不需要的列
            subject = cells[2].get_text(strip=True)
            score = cells[5].get_text(strip=True)
            credit = cells[3].get_text(strip=True)
            data.append([subject, score, credit])
    return data

# 將資料寫入CSV檔案
def write_to_csv(data, filename):
    with open(filename, 'w', newline='', encoding='utf-8-sig') as file:
        writer = csv.writer(file)
        #writer.writerow(['科目名稱', '成績', '學分'])  # 寫入表頭
        writer.writerows(data)

# 使用GUI介面選取HTML檔案
Tk().withdraw()  # 隱藏Tk窗口
html_file_path = filedialog.askopenfilename(title="選擇HTML檔案", filetypes=[("HTML files", "*.html")])

# 讀取HTML檔案
with open(html_file_path, 'r', encoding='big5') as file:
    html = file.read()

# 解析HTML並提取資料
table = parse_html(html)
data = extract_data(table)

# 將資料寫入CSV檔案
csv_file_path = html_file_path.replace('.html', '.csv')
write_to_csv(data, csv_file_path)

print(f"資料已成功提取並儲存為 {csv_file_path}")

app = GradeCalculatorApp()
app.run()
