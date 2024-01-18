import pandas as pd
import numpy as np

student_test = [410470443, 410580157, 410580236]
problem_list = ['001', '002', '003', '004', '005', '006', '007', '008', '009']
column = ['HW_1', 'HW_2', 'HW_3', 'HW_4', 'HW_5', 'HW_6', 'HW_7', 'HW_8', 'HW_9']

class XLSX:
    def __init__(self, debug = True):
        self.debug = debug

    def read_first_column(self, file_path):
        try:
            df = pd.read_excel(file_path)
            students_number = df.iloc[:, 0].tolist()
            print(students_number)
            return students_number

        except Exception as e:
            print(f"An error occurred: {e}")
            return None
 
    def write_xlsx(self, students_list, AC_list, file_path):
        df = pd.read_excel(file_path) 
        for i in range(len(students_list)):
        #for i in range(3):
            student_ID = df[df['學號'] == students_list[i]]
            for p in range(9):
                if problem_list[p] in AC_list[i]:
                    for index in student_ID.index:
                        df.at[index, column[p]] = 100


        print(df)
        df.to_excel('updated_score_crw.xlsx', index=False)
        return None

        



