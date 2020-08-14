import openpyxl
import generator

wb = openpyxl.load_workbook('Приложение №2.xlsx')
sheets = wb.sheetnames

auditoriums = []
programms = []
for j in range(2):
    if j == 0:
        sheet = wb['параметры аудиторий']
        for i in range(2, 13):
            auditoriums.append(
                generator.ClassRoom(sheet['A{}'.format(i)], sheet['B{}'.format(i)], sheet['C{}'.format(i)],
                                    sheet['D{}'.format(i)], sheet['E{}'.format(i)], sheet['F{}'.format(i)]))
    elif j == 1:
        sheet = wb['параметры программ']
        x_ = sheet['B2'].value
        for i in range(2, 42):
            x = sheet['B{}'.format(i)].value
            if x:
                x = str(x).replace('\n', '')
            programms.append(
                generator.Program(sheet['A{}'.format(i)], x, sheet['C{}'.format(i)], sheet['D{}'.format(i)],
                                  sheet['E{}'.format(i)], sheet['F{}'.format(i)], sheet['G{}'.format(i)],
                                  sheet['H{}'.format(i)], sheet['I{}'.format(i)], sheet['J{}'.format(i)],
                                  sheet['K{}'.format(i)], sheet['L{}'.format(i)], sheet['M{}'.format(i)]))

            
