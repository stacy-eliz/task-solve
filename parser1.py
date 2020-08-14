import openpyxl

wb = openpyxl.load_workbook('Приложение №1.xlsx')
sheets = wb.sheetnames

direction = []
weeks = []
sheet = wb['ДПО']

for column in sheet.iter_cols(6, 7):
    for j in column:
        x = j.value
        if x != None:
            direction.append(str(x).replace('\n', ' ').strip())

for column in sheet.iter_cols(8, sheet.max_column):
    weeks.append([])
    for j in column:
        if j.value != None:
            x = str(j.value).replace('\n', ' ').strip()
            if not x.isupper() and x[0].isalpha():
                if 'ауд.' in x:
                    y = x.find('ауд.')
                    x = x[:y + 4]
                weeks[-1].append(x)
    if weeks[-1] == [] or weeks[-1] == ['Неделя 52 23.12-29.12'] or weeks[-1] == ['Неделя 01 30.12-05.01']:
        weeks.pop()

# for j in weeks:
#     print(j)
#
# print(direction)

