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
##for i in b:
##    print(i.name, i.programme)
for i in range(1, len(a)):    
    for j in range(len(a[i])):
##        print(a[i][j], j)
        if not(type(a[i][j])is list) and a[i][j]!= None and a[0][j] != None:         
            for k in range(len(b)):
                d = shorter(a[i][j]).replace("Повышение", "повышения")
                d = d.lower()
                if a[0][j].lower() in b[k].name.lower() or b[k].name.lower() in  a[0][j].lower():     
                    if d in b[k].programme.lower() or b[k].programme.lower() in d:
                        for l in range(len(c)):
                            h = b[k].features.lower().replace("требуется ","").replace("нет","")
    ##                          print(c[l].name, h)
                            if str(c[l].name) in h:
                                if c[l].is_busy:
                                    f = Shedule1.get_free_rooms()
                                    if len(f)!=0:
                                        # print("swaping **** ",c[l], f[0])
                                        f[0].is_busy=1
                                        Shedule1.Add_Room(f[0], a[i][2], None, b[k].name)
                                        Shedule1.swap_rooms(c[l],f[0],a[i][2])  
                                        # print(Shedule1.busy_room[(c[l].name, a[i][2])], Shedule1.busy_room[(f[0].name, a[i][2])])
                                else:      
                                    Shedule1.Add_Room(c[l], a[i][2], None, a[i][j]);
                                    # print("not swap", Shedule1.busy_room[(c[l].name, a[i][2])], c[l].name)
                            elif h in c[l].differences.lower() and not(c[l].is_busy):  
                                Shedule1.Add_Room(c[l], a[i][2], None, a[i][j]);
                                c[l].is_busy = 1;
                                break;
        elif type(a[i][j]) is list:
            for g in range(len(a[i][j])):
                # for k in range(len(b)):
                #     print(b[k], b[k].features)
                for k in range(len(b)):
                    d = shorter(a[i][j][g]).replace("Повышение", "повышения")
                    d = d.lower()
##                    print(b[k].features)
                    if a[0][j][g].lower() in b[k].name.lower() or b[k].name.lower() in  a[0][j][g].lower():     
                        if d in b[k].programme.lower() or b[k].programme.lower() in d:
                            for l in range(len(c)):
                                
                                h = b[k].features.lower().replace("требуется ","").replace("нет","")
        ##                          print(c[l].name, h)
                                if str(c[l].name) in h:
                                    if c[l].is_busy:
                                        f = Shedule1.get_free_rooms()
                                        if len(f)!=0:
                                            # print("swaping **** ",c[l], f[0])
                                            f[0].is_busy=1
                                            Shedule1.Add_Room(f[0], a[i][2], None, b[k].name)
                                            Shedule1.swap_rooms(c[l],f[0],a[i][2])  
                                            # print(Shedule1.busy_room[(c[l].name, a[i][2])], Shedule1.busy_room[(f[0].name, a[i][2])])
                                    else:      
                                        Shedule1.Add_Room(c[l], a[i][2], None, a[i][j][g]);
                                        # print("not swap", Shedule1.busy_room[(c[l].name, a[i][2])], c[l].name)
                                elif h in c[l].differences.lower() and not(c[l].is_busy):  
                                    Shedule1.Add_Room(c[l], a[i][2], None, a[i][j][g]);
                                    c[l].is_busy = 1;
                                    break;
                
                
                        
                                
    
    Shedule1.leave_rooms()             
                    
##print(b)
##print(c)
##print(a)
# for i in Shedule1.busy_room:
#     print(i, Shedule1.busy_room[i])

