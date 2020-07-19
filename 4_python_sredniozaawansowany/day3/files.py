import csv
import json
from collections import defaultdict
# file_name = 'salary.csv'    # input('Podaj nazwę pliku: ')
#
# with open(file_name) as in_file, open('salary2.csv', 'w') as out_file:
#     reader = csv.reader(in_file)
#     writer = csv.writer(out_file, lineterminator='\n')
#
#     # row = next(reader)
#     # row.append('new_salary')
#     # writer.writerow(row)
#
#     for idx, row in enumerate(reader):
#         if idx == 0:
#             row.append('new_salary')
#         else:
#             row.append(int(row[1]) * 1.1)
#         writer.writerow(row)
#
#
# import pandas as pd
# csv_input = pd.read_csv('salary.csv')
# csv_input['new_salary'] = csv_input['salary'] * 1.1
# csv_input.to_csv('output.csv', index=False)


# with open('employee.json') as in_file, open('employee2.json', 'w') as out_file:
#     data = json.load(in_file)
#     for empl in data:
#         empl['new_salary'] = empl['salary'] * 1.1
#     json.dump(data, out_file, indent=2)



def del_userID(user):
    del user["userId"]
    return user

with open('users.json') as in_file:
    data = json.load(in_file)

with open('completed.csv', 'w') as out_file:
    writer = csv.writer(out_file, lineterminator='\n')
    writer.writerow(data[0].keys())
    aggregate_data = defaultdict(list)
    for user in data:
        if user['completed']:
            writer.writerow(user.values())
            aggregate_data[f'user_{user["userId"]}'].append(del_userID(user))

with open('aggregate_users.json', 'w') as out_file:
    json.dump(aggregate_data, out_file, indent=2)
