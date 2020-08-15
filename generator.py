import classes
from parser2 import application2_audit, application2_programm
from parser1 import application1
from reading_teachers import Full_teacher
import re
from reading_teachers import Full_teacher
import matplotlib.pyplot as plt
import numpy as np



        

Shedule1 = classes.Shedule()
path_app1 = "app1.xlsx"
a = application1(path_app1)
path = "app2.xlsx"
b = application2_programm(path) #массив объектов программ
c = application2_audit(path) #массив объектов аудиторий
s = 0

counter_weeks = 0
count_free_room_weeks = 0

count_free_room_week = 0

y1 = []
y2 = []


##def shorter(st):
####    print(type(st))
##    for i in range(len(st)):
##        if st[i].isnumeric():
##            
##            return st[:i]










##path_app1 = "app1.xlsx"
##path = "app2.xlsx"
##a = application1(path_app1)
##b = Full_teacher(path)
def shorter(st, f):
    if f:
        for i in range(len(st)):
            if st[i].isnumeric():
                return st[:i]
    else:
        for i in range(len(st)):
            if st[i].isnumeric():
                return st[i:][:11]

teachers = Full_teacher('app2.xlsx')

for i in range(1, len(a)):
    for j in range(len(a[i])):
        if a[i][j] != None and not 'Неделя' in a[i][j]:
            if isinstance(a[i][j], list):
                pass
            else:
                for m in teachers:
                    x = m.disciplin.replace('Управление безопасностью полетов', 'Безопасность полетов').replace('Организация пассажирских перевозок', 'Пассажирские перевозки')
                    if x in a[0][j] or a[0][j] in x:
                        Shedule1.Add_Teacher(m, shorter(a[i][j], 0), x, a[i][j])
    Shedule1.leave_teachers()

for i in Shedule1.busy_teachers:
    print(i, Shedule1.busy_teachers[i])
















##a = [[0 for i in range(52)] for j in range(8)] #расписание годовое

##for i in b:
##    print(i.name, i.programme)
for i in range(1, len(a)):
    counter_weeks +=1        
    for j in range(len(a[i])):
        if not(type(a[i][j])is list) and a[i][j]!= None and a[0][j] != None:         
            for k in range(len(b)):
                if "Опасные грузы" in a[0][j]:
                    
                    cate = a[0][j].replace("Опасные грузы.","").replace(" категория","")
##                    print(a[i][j])
##                    print(b[k].name)
                    if "опасные грузы" in b[k].name.lower():
                        cate+= " категория ИКАО/ИАТА"
##                        print(cate)
                        if "Базовый" in a[i][j]:
                            cate+=".базовый курс"
                        if cate.lower() in b[k].programme.lower() or b[k].programme.lower() in cate.lower():
##                            print("1")
                            f = Shedule1.get_free_rooms()
                            if len(f)!=0:
                                for s in f:
##                                    print("DANGEROUSE!!!")
                                    s.is_busy = 1
                                    Shedule1.Add_Room(s, a[i][2], None, b[k].name)
##                                    print(s)
                                    break;
                        
                        
                else:                
                    d = shorter(a[i][j], True).replace("Повышение", "повышения")
                    d = d.lower()
                    if a[0][j].lower() in b[k].name.lower() or b[k].name.lower() in  a[0][j].lower():     
                        if d in b[k].programme.lower() or b[k].programme.lower() in d:
                            for l in range(len(c)):
                                h = b[k].features.lower().replace("требуется ","").replace("нет","")
                                if str(c[l].name) in h:
                                    if c[l].is_busy:
                                        f = Shedule1.get_free_rooms()
                                        if len(f)!=0:
                                            for s in f:
                                                s.is_busy = 1
                                                Shedule1.Add_Room(s, a[i][2], None, b[k].name)
                                                Shedule1.swap_rooms(c[l],s,a[i][2])  
                                                break;                                           
                                    else:      
                                        Shedule1.Add_Room(c[l], a[i][2], None, a[i][j]);
                                elif h in c[l].differences.lower() and not(c[l].is_busy):  
                                    Shedule1.Add_Room(c[l], a[i][2], None, a[i][j]);
                                    c[l].is_busy = 1;
                                    break;
        elif type(a[i][j]) is list:
            for g in range(len(a[i][j])):
                for k in range(len(b)):
                    d = shorter(a[i][j][g], True).replace("Повышение", "повышения")
                    d = d.lower()
                    if a[0][j][g].lower() in b[k].name.lower() or b[k].name.lower() in  a[0][j][g].lower():     
                        if d in b[k].programme.lower() or b[k].programme.lower() in d:
                            for l in range(len(c)):                               
                                h = b[k].features.lower().replace("требуется ","").replace("нет","")
                                if str(c[l].name) in h:
                                    if c[l].is_busy:
                                        f = Shedule1.get_free_rooms()
                                        if len(f)!=0:
                                            for s in f:
                                                s.is_busy = 1
                                                Shedule1.Add_Room(s, a[i][2], None, b[k].name)
                                                Shedule1.swap_rooms(c[l],s,a[i][2])  
                                                break;
                                    else:      
                                        Shedule1.Add_Room(c[l], a[i][2], None, a[i][j][g]);
                                elif h in c[l].differences.lower() and not(c[l].is_busy):  
                                    Shedule1.Add_Room(c[l], a[i][2], None, a[i][j][g]);
                                    c[l].is_busy = 1;
                                    break;
    
##    if type(a[i][2]) is str and "Неделя" in a[i][2]:
##        print(i, a[i][2], len(Shedule1.get_free_rooms()))
##        if len(Shedule1.get_free_rooms())>=100:
##            print(Shedule1.get_free_rooms())
        
    if i%2==0:            
        count_free_room_week=len(Shedule1.get_free_rooms())         
        y2.append(count_free_room_week/11*100)
                      
    count_free_room_weeks+=len(Shedule1.get_free_rooms())
    if counter_weeks==4:
        y1.append(count_free_room_weeks/44*100)
        counter_weeks = 0
        count_free_room_weeks = 0
    
    Shedule1.leave_rooms()
##for i in Shedule1.busy_room:
##    print(i)
def graf_tadjyk1(y1): 
    x1 = [i for i in range(1,27)]
    y1 = np.array(y1)
    x1 = np.array(x1)
    plt.title("Процентные данные загруженности аудиторий на каждые 4 недели")
    plt.plot( x1,y1)
    plt.scatter(x1, y1)
    plt.grid()
    ##plt.savefig("tadjyk1.png")
    plt.show()

def graf_tadjyk2(y2):
    x2 = [i for i in range(1,54)]
    y2 = np.array(y2)
    x2 = np.array(x2)
    plt.title("Процентные данные загруженности аудиторий на каждую неделю")
    plt.plot( x2,y2)
    plt.scatter(x2, y2)
    plt.grid()
    ##plt.savefig("tadjyk2.png")
    plt.show()

graf_tadjyk1(y1)
graf_tadjyk2(y2)


