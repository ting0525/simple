from control_xlsx import XLSX
from crw import crawler

excel_file_path = 'score_crw.xlsx'

if __name__ == "__main__":
    group_member = XLSX()  
    students_number = group_member.read_first_column(excel_file_path) 
    # print('students_number', len(students_number)) 
    crawler_AC = crawler()
    AC_list = crawler_AC.crawling(students_number)
    # print('AC_list = ', AC_list)
    
    score_xlsx = XLSX()
    score_xlsx.write_xlsx(students_number, AC_list, excel_file_path)





