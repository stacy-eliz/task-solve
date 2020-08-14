class Teacher:
    def __init__(self, number=None, name=None, program=None, antiprogram = None, prioritet = None, smeni = None):
        """Constructor"""
        self.number = number
        self.program = program
        self.name = name
        self.antiprogram = antiprogram
        self.smeni = smeni

class ClassRoom:
    def __init__(self, name=None, places=None, type_of_discipline=None, differences=None, prioritet_discipline=None, anti_discipline=None):
        """Constructor"""
        self.name = name
        self.places = places
        self.type_of_discipline = type_of_discipline
        self.differences = differences
        self.prioritet_discipline = prioritet_discipline
        self.anti_discipline = anti_discipline

class Program:
    def __init__(self, number_of_program=None, name=None, hours=None, hours_proizv=None, hours_distant=None, day_offline=None, count_of_groups=None, count_of_worker=None, count_of_listener=None, count_of_teacher=None, count_of_classroom=None):
        self.number_of_program = number_of_program
        self.name = name
        self.hours = hours
        self.hours_proizv = hours_proizv
        self.hours_distant = hours_distant
        self.day_offline = day_offline
        self.count_of_groups = count_of_groups
        self.count_of_worker = count_of_worker
        self.count_of_listener = count_of_listener
        self.count_of_teacher = count_of_teacher
        self.count_of_classroom = count_of_classroom


Teach = Teacher('20435', 'Лебедев', [1, 2], [])