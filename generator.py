import classes
from parser2 import application2_audit, application2_programm
from parser1 import application1
from reading_teachers import Full_teacher
import re



        

Shedule1 = classes.Shedule()
def shorter(st):
    for i in range(len(st)):
        if st[i].isnumeric():
            return st[:i]



##a = [[0 for i in range(52)] for j in range(8)] #расписание годовое
path_app1 = "app1.xlsx"
a = application1(path_app1)
path = "app2.xlsx"
b = application2_programm(path) #массив классов программ
c = application2_audit(path) #массив классов аудиторий
##for i in b:
##    print(i.name, i.programme)
for i in range(1, len(a)):
    
    for j in range(len(a[i])):
##        print(a[i][j], j)
        if a[i][j]!= None and a[0][j] != None:
            for k in range(len(b)):
                d = shorter(a[i][j]).replace("Повышение", "повышения")
                d = d.lower()
                if a[0][j].lower() in b[k].name.lower() or b[k].name.lower() in  a[0][j].lower():
##                    print("1")
                    
##                    print(d, "*", b[k].programme)
                    if d in b[k].programme.lower() or b[k].programme.lower() in d:
##                        print("2")
                        for l in range(len(c)):
                            
                            if b[k].features.lower().replace("требуется ","").replace("нет","") in c[l].differences.lower() and not(c[l].is_busy):
##                                print("3", c[l])
                                Shedule1.Add_Room(c[l], a[i][2], None, a[i][j]);
                                c[l].is_busy = 1;
                                break;
                        
                    
##print(b)
##print(c)
##print(a)
print(Shedule1)

