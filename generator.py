import classes
from parser2 import application2_audit, application2_programm
from parser1 import application1
from reading_teachers import Full_teacher
import re



        

Shedule1 = classes.Shedule()
def shorter(st):
##    print(type(st))
    for i in range(len(st)):
        if st[i].isnumeric():
            
            return st[:i]



##a = [[0 for i in range(52)] for j in range(8)] #расписание годовое
path_app1 = "app1.xlsx"
a = application1(path_app1)
path = "app2.xlsx"
b = application2_programm(path) #массив объектов программ
c = application2_audit(path) #массив объектов аудиторий
count_free_room_week = 0
counter_week = 0
##for i in b:
##    print(i.name, i.programme)
for i in range(1, len(a)):
    counter_week +=1        
    for j in range(len(a[i])):
        if not(type(a[i][j])is list) and a[i][j]!= None and a[0][j] != None:         
            for k in range(len(b)):
                d = shorter(a[i][j]).replace("Повышение", "повышения")
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
                    d = shorter(a[i][j][g]).replace("Повышение", "повышения")
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
        
                
                
                      
    count_free_room_week+=len(Shedule1.get_free_rooms())
    if counter_week==4:
        print("%.2f" % (count_free_room_week/44*100), "%")
        counter_week = 0
        count_free_room_week = 0
    
    Shedule1.leave_rooms()             
                    
##print(b)
##print(c)
##print(a)
##for i in Shedule1.busy_room:
##    print(i, Shedule1.busy_room[i])

