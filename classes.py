class Teacher:
    def __init__(self, number=None, name=None, program=None, antiprogram=None, prioritet=None, smeni=None,
                 disciplin=None):
        """Constructor"""
        self.number = number
        self.program = program
        self.disciplin = disciplin
        self.name = name
        self.prioritet = prioritet
        self.antiprogram = antiprogram
        self.smeni = smeni
        self.is_busy = 0

    def __str__(self):
        return ('Teacher: ' + str(self.name))

    def __repr__(self):
        return ('Teacher: ' + str(self.name))

    def leave(self):
        self.is_busy = 0


class ClassRoom:

    def __init__(self, name=None, places=None, type_of_discipline=None, differences=None, prioritet_discipline=None,
                 anti_discipline=None):
        """Constructor"""
        self.name = name
        self.places = places
        self.type_of_discipline = type_of_discipline
        self.differences = differences
        self.prioritet_discipline = prioritet_discipline
        self.anti_discipline = anti_discipline
        self.is_busy = 0

    def __str__(self):
        return ('ClassRoom: ' + str(self.name))

    def __repr__(self):
        return ('ClassRoom: ' + str(self.name))

    def leave(self):
        self.is_busy = 0


class Program:
    def __init__(self, number_of_program=None, name=None, programme=None, features=None, hours=None, hours_proizv=None,
                 hours_distant=None, day_offline=None, count_of_groups=None, count_of_worker=None,
                 count_of_listener=None, count_of_teacher=None, count_of_classroom=None):
        self.number_of_program = number_of_program
        self.name = name
        self.programme = programme
        self.features = features
        self.hours = hours
        self.hours_proizv = hours_proizv
        self.hours_distant = hours_distant
        self.day_offline = day_offline
        self.count_of_groups = count_of_groups
        self.count_of_worker = count_of_worker
        self.count_of_listener = count_of_listener
        self.count_of_teacher = count_of_teacher
        self.count_of_classroom = count_of_classroom

    def __str__(self):
        return ('Programm: ' + str(self.name) + ' Hourse: ' + str(self.hours))

    def __repr__(self):
        return ('Programm: ' + str(self.name) + ' Hourse: ' + str(self.hours))


class Shedule:
    def __init__(self):
        self.busy_room = {}
        self.rooms = set()
        self.busy_teachers = {}
        self.teachers = set()

    def Add_Room(self, room, date, time, programme_name):
        self.busy_room[(room.name, date)] = [time, programme_name]

        self.rooms.add(room)

    def __str__(self):
        return (str(self.busy_room))

    def __repr__(self):
        return (str(self.busy_room))

    def leave_rooms(self):
        for i in self.rooms:
            i.leave()

    def swap_rooms(self, room1, room2, date1, date2=None):
        if date2 == None:
            date2 = date1
        self.busy_room[(room1.name, date1)], self.busy_room[(room2.name, date2)] = self.busy_room[(room2.name, date2)], \
                                                                                   self.busy_room[(room1.name, date1)]

    def get_free_rooms(self):
        f = set()
        for i in self.rooms:
            if not i.is_busy:
                f.add(i)
        return f

    def Add_Teacher(self, teacher, date, disciplin, programme_name, count_week):
        self.busy_teachers[(teacher.name, date)] = [disciplin, programme_name, count_week]

        self.teachers.add(teacher)

    def __str__(self):
        return (str(self.busy_room), str(self.busy_teachers))

    def __repr__(self):
        return (str(self.busy_room), str(self.busy_teachers))

    def leave_teachers(self):
        for i in self.teachers:
            i.leave()