import classes
from parser2 import application2_audit, application2_programm
from parser1 import application1
from reading_teachers import Full_teacher



        

Shedule1 = classes.Shedule()



##a = [[0 for i in range(52)] for j in range(8)] #расписание годовое
path_app1 = "app1.xlsx"
a = application1(path_app1)
path = "app2.xlsx"
b = application2_programm(path) #массив классов программ
c = application2_audit(path) #массив классов аудиторий
for i in range(len(a)):
    for j in range(len(a[i])):
        for k in range(len(b)):
            if a[i][j] in b[k].name or b[k].name in a[i][j]:
                for l in range(len(c)):
                    if b[k].features in c[l].differences and not(c[l].is_busy):
                        Shedule1.Add_Room(c[l].name, a[i][0], None, a[i][j])
                        c[l].is_busy = 1
                        break;
print(b)
print(c)
print(Shedule1)

