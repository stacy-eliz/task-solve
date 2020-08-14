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
            if ', ' in str(sheet['A{}'.format(i)].value):
                x = str(sheet['A{}'.format(i)].value).split(',')
                for j in x:
                    j = j.strip()
                    auditoriums.append(
                        generator.ClassRoom(j, sheet['B{}'.format(i)].value, sheet['C{}'.format(i)].value,
                                            sheet['D{}'.format(i)].value, sheet['E{}'.format(i)].value,
                                            sheet['F{}'.format(i)].value))
            else:
                auditoriums.append(
                    generator.ClassRoom(sheet['A{}'.format(i)].value, sheet['B{}'.format(i)].value,
                                        sheet['C{}'.format(i)].value,
                                        sheet['D{}'.format(i)].value, sheet['E{}'.format(i)].value,
                                        sheet['F{}'.format(i)].value))
    elif j == 1:
        sheet = wb['параметры программ']
        for i in range(2, 42):
            x = sheet['B{}'.format(i)].value
            if x:
                x = str(x).replace('\n', '')
            programms.append(
                generator.Program(sheet['A{}'.format(i)].value, x, sheet['C{}'.format(i)].value,
                                  sheet['D{}'.format(i)].value,
                                  sheet['E{}'.format(i)].value, sheet['F{}'.format(i)].value,
                                  sheet['G{}'.format(i)].value,
                                  sheet['H{}'.format(i)].value, sheet['I{}'.format(i)].value,
                                  sheet['J{}'.format(i)].value,
                                  sheet['K{}'.format(i)].value, sheet['L{}'.format(i)].value,
                                  sheet['M{}'.format(i)].value))
                
print(programms)


            
