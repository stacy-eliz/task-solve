import openpyxl
from pathlib import Path
from classes import Teacher
def Full_teacher(path) -> [Teacher]:
  xlsx_file = Path(path)
  wb_obj = openpyxl.load_workbook(xlsx_file)
  sheet = wb_obj.active
  pr = []
  NUMBERS_OF_PROGRAMS = []
  for row in sheet.iter_rows(min_row=2):
    pr.append(str(row[3].value).split(';'))
  flatten = lambda l: [item for sublist in l for item in sublist]
  for i in list(set(flatten(pr))):
    NUMBERS_OF_PROGRAMS.append(i)
  del pr
  teachers = [Teacher()] * sheet.max_row
  i = 0
  for row in sheet.iter_rows(min_row=2):
    antipr = NUMBERS_OF_PROGRAMS
    teachers[i].number = row[0].value
    teachers[i].name = row[1].value
    teachers[i].program = str(row[3].value).split(';')
    azaza = []
    [azaza.append(j) for j in NUMBERS_OF_PROGRAMS if j not in teachers[i].program]
    teachers[i].antiprogram = azaza
    del azaza
    teachers[i].smeni = row[7].value
    i+=1
  return teachers