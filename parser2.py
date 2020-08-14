import openpyxl
import generator


def application2_audit(path):
    wb = openpyxl.load_workbook(path)  # 'Приложение №2.xlsx'

    auditoriums = []
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
    return auditoriums


def application2_programm(path):
    wb = openpyxl.load_workbook(path)  # 'Приложение №2.xlsx'

    programms = []
    sheet = wb['параметры программ']
    out = sheet['B2'].value
    for i in range(2, 42):
        x_ = sheet['B{}'.format(i)].value
        if x_:
            out = x_.replace('\n', ' ')
        programms.append(
            generator.Program(sheet['A{}'.format(i)].value, out, sheet['C{}'.format(i)].value,
                              sheet['D{}'.format(i)].value,
                              sheet['E{}'.format(i)].value, sheet['F{}'.format(i)].value,
                              sheet['G{}'.format(i)].value,
                              sheet['H{}'.format(i)].value, sheet['I{}'.format(i)].value,
                              sheet['J{}'.format(i)].value,
                              sheet['K{}'.format(i)].value, sheet['L{}'.format(i)].value,
                              sheet['M{}'.format(i)].value))
    return programms
