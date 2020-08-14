import openpyxl

wb = openpyxl.load_workbook('Приложение №2.xlsx')
sheets = wb.sheetnames

name1 = []
places = []
type_of_discipline = []
differences = []
prioritet_discipline = []
anti_discipline = []

discipline = []
curriculum = []
features = []
hours = []
hours_proizv = []
hours_distant = []
day_offline = []
count_of_groups = []
count_of_worker = []
count_of_listener = []
count_of_teacher = []
count_of_classroom = []
number_of_program = []

for j in range(2):
    if j == 0:
        sheet = wb['параметры аудиторий']
        t = None
        for i in ['A', 'B', 'C', 'D', 'E', 'F']:
            for j in range(2, 13):
                if i == 'A':
                    t = name1
                elif i == 'B':
                    t = places
                elif i == 'C':
                    t = type_of_discipline
                elif i == 'D':
                    t = differences
                elif i == 'E':
                    t = prioritet_discipline
                elif i == 'F':
                    t = anti_discipline
                t.append(sheet['{}{}'.format(i, j)].value)
    elif j == 1:
        sheet = wb['параметры программ']
        t = None
        for i in ['B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N']:
            for j in range(2, 42):
                if i == 'B':
                    t = discipline
                elif i == 'C':
                    t = curriculum
                elif i == 'D':
                    t = features
                elif i == 'E':
                    t = hours
                elif i == 'F':
                    t = hours_proizv
                elif i == 'G':
                    t = hours_distant
                elif i == 'H':
                    t = day_offline
                elif i == 'I':
                    t = count_of_groups
                elif i == 'J':
                    t = count_of_worker
                elif i == 'K':
                    t = count_of_listener
                elif i == 'L':
                    t = count_of_teacher
                elif i == 'M':
                    t = count_of_classroom
                elif i == 'N':
                    t = number_of_program
                x = sheet['{}{}'.format(i, j)].value
                if x:
                    x = str(x).replace('\n', '')
                else:
                    x = t[-1]
                t.append(x)
