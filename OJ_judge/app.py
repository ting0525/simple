import json
import requests
import pandas as pd
from tqdm import tqdm
cookies = {
    '_ga': 'GA1.2.1986989855.1704629576',
    '_gid': 'GA1.2.444004720.1705590117',
    'csrftoken': 'IMObVxjw5kZF8Lhcx4hzt2ePNnbynCRiTJT1O7ACt73n2qfFIEk4WQQWGcxXXRvI',
    'sessionid': 'hsffwdhgc1nd3595zt9qpo3geld0qind',
    '_ga_59QEB25NR7': 'GS1.2.1705590117.2.1.1705590230.0.0.0'
}
with open('student_ids.json', 'r') as f:
    student_ids = json.load(f)['student_ids']

report_csv_data = {}
for student_id in tqdm(student_ids):
    res = requests.get(f"https://oj.zxzinn.com/api/profile?username={student_id}", cookies=cookies)
    check_list = [0 for i in range(9)]
    try:
        for index, problem in res.json()['data']['acm_problems_status']['problems'].items():
            if problem['_id'] == '1':
                continue
            check_list[int(problem['_id']) - 1] = 1
    except:
        ...
    report_csv_data[student_id] = check_list
report_csv = pd.DataFrame(report_csv_data).T
report_csv.columns = [f'HW_{i}' for i in range(1, 10)]
report_csv['solution_num'] = report_csv.sum(axis=1)
report_csv.to_csv("report_csv.csv")
