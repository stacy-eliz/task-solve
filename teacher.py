import classes
from reading_teachers import Full_teacher
from parser1 import application1
from generator import Shedule1

path_app1 = "app1.xlsx"
path = "app2.xlsx"
a = application1(path_app1)
b = Full_teacher(path)  # массив классов преподавателей


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
                    x = m.disciplin.replace('Управление безопасностью полетов', 'Безопасность полетов').replace(
                        'Организация пассажирских перевозок', 'Пассажирские перевозки')
                    if x in a[0][j] or a[0][j] in x:
                        Shedule1.Add_Teacher(m, shorter(a[i][j], 0), x, a[i][j])
    Shedule1.leave_teachers()
print(Shedule1.busy_teachers)
'''[Teacher: Лебедев М.В., Teacher: Красненко А.Г., Teacher: Морозов И.О., Teacher: Корнеев Р.Л., Teacher: Чернов Д.А., Teacher: Автеньев Д.Г., Teacher: Шабалин К.Н., Teacher: Пачко Г.М., Teacher: Гладковская А.Ю., Teacher: Попова И.О., Teacher: Миньков А.С., Teacher: Монахов Г.П., Teacher: Умняшкин О.В., Teacher: Крылова С.А., Teacher: Красиков А.В., Teacher: Щеглов А.В., Teacher: Джавадян А.Э., Teacher: Морозов Д.В., Teacher: Кузнецов А.А., Teacher: Некрасова Л.Д., Teacher: Биднюк В.Д., Teacher: Блинов А.Б., Teacher: Казаков-Прокопьев Т.А., Teacher: Селезнев А.В., Teacher: Вишняков И.А., Teacher: Шарипов А.В., Teacher: Митяев В.В., Teacher: Патешкин В.Ю., Teacher: Каребчик В.А., Teacher: Кушниренко П.В., Teacher: Четыркин И.А., Teacher: Суббота П.В., Teacher: Фетисов В.А., Teacher: Давыдова Г.В.]
'''
